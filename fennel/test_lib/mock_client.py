import json
from collections import defaultdict
from concurrent import futures
from dataclasses import dataclass
from functools import partial
from typing import Dict, List, Optional, Union

import grpc
import pandas as pd
import pyarrow as pa
from requests import Response

import fennel.datasets.datasets
from fennel.client import Client
from fennel.datasets import Dataset, Pipeline
from fennel.featuresets import Featureset, Feature, Extractor
from fennel.gen.dataset_pb2 import CreateDatasetRequest
from fennel.gen.services_pb2_grpc import (
    add_FennelFeatureStoreServicer_to_server,
    FennelFeatureStoreStub,
    FennelFeatureStoreServicer,
)
from fennel.lib.graph_algorithms import (
    get_extractor_order,
    is_extractor_graph_cyclic,
)
from fennel.test_lib.executor import Executor

TEST_PORT = 50051
TEST_DATA_PORT = 50052


class FakeResponse(Response):
    def __init__(self, status_code: int, content: str):
        self.status_code = status_code

        self.encoding = "utf-8"
        if status_code == 200:
            self._ok = True
            self._content = json.dumps({}).encode("utf-8")
            return
        self._content = json.dumps({"error": f"{content}"}, indent=2).encode(
            "utf-8"
        )


def lookup_fn(
    data: Dict[str, pd.DataFrame],
    datasets: Dict[str, Dataset],
    cls_name: str,
    ts: pa.Array,
    properties: List[str],
    keys: pa.RecordBatch,
):
    key_df = keys.to_pandas()
    if cls_name not in data:
        timestamp_col = datasets[cls_name].timestamp_field
        # Create a dataframe with all nulls
        val_cols = datasets[cls_name].fields()
        if len(properties) > 0:
            val_cols = [
                x for x in val_cols if x in properties or x in key_df.columns
            ]
        val_cols.remove(timestamp_col)
        empty_df = pd.DataFrame(
            columns=val_cols, data=[[None] * len(val_cols)] * len(key_df)
        )
        return pa.RecordBatch.from_pandas(empty_df)
    right_df = data[cls_name]
    timestamp_field = datasets[cls_name].timestamp_field
    join_columns = key_df.columns.tolist()
    key_df[timestamp_field] = ts.to_pandas()
    # Sort the keys by timestamp
    key_df = key_df.sort_values(timestamp_field)
    df = pd.merge_asof(
        left=key_df,
        right=right_df,
        on=timestamp_field,
        by=join_columns,
        direction="backward",
    )
    # drop the timestamp column
    df = df.drop(columns=[timestamp_field])
    if len(properties) > 0:
        df = df[properties]
    return pa.RecordBatch.from_pandas(df)


@dataclass
class _DatasetInfo:
    fields: List[str]
    timestamp_field: str


class MockClient(Client):
    def __init__(self, stub, server: Optional[grpc.Server] = None):
        super().__init__(url=f"localhost:{TEST_PORT}")
        self.stub = stub

        self.dataset_requests: Dict[str, CreateDatasetRequest] = {}
        self.datasets: Dict[str, _DatasetInfo] = {}
        # Map of dataset name to the dataframe
        self.data: Dict[str, pd.DataFrame] = {}
        # Map of datasets to pipelines it is an input to
        self.listeners: Dict[str, List[Pipeline]] = defaultdict(list)
        fennel.datasets.datasets.dataset_lookup = partial(
            lookup_fn, self.data, self.datasets
        )
        self.extractors: List[Extractor] = []
        self.server = server

    # ----------------- Public methods -----------------

    def log(self, dataset_name: str, df: pd.DataFrame):
        if dataset_name not in self.dataset_requests:
            return FakeResponse(404, f"Dataset {dataset_name} not found")
        dataset = self.dataset_requests[dataset_name]
        with pa.ipc.open_stream(dataset.schema) as reader:
            dataset_schema = reader.schema
            try:
                pa.RecordBatch.from_pandas(df, schema=dataset_schema)
            except Exception as e:
                content = (
                    f"Dataframe does not match schema for dataset "
                    f"{dataset_name}: {str(e)}"
                )
                return FakeResponse(status_code=400, content=content)

            self._merge_df(df, dataset_name)

            for pipeline in self.listeners[dataset_name]:
                executor = Executor(self.data)
                ret = executor.execute(pipeline)
                if ret is None:
                    continue
                # Recursively log the output of the pipeline to the datasets
                resp = self.log(pipeline.dataset_name, ret.df)
                if resp.status_code != 200:
                    return resp
        return FakeResponse(200, "OK")

    def sync(
        self, datasets: List[Dataset] = [], featuresets: List[Featureset] = []
    ):

        for dataset in datasets:
            self.dataset_requests[
                dataset.name
            ] = dataset.create_dataset_request_proto()
            self.datasets[dataset.name] = _DatasetInfo(
                dataset.fields(), dataset.timestamp_field
            )
            for pipeline in dataset._pipelines:
                for input in pipeline.inputs:
                    self.listeners[input.name].append(pipeline)

        for featureset in featuresets:
            self.extractors.extend(featureset.extractors)

        if is_extractor_graph_cyclic(self.extractors):
            raise Exception("Cyclic graph detected in extractors")

    def extract_features(
        self,
        input_feature_list: List[Union[Feature, Featureset]],
        output_feature_list: List[Union[Feature, Featureset]],
        input_df: pd.DataFrame,
        timestamps: Optional[pd.Series] = None,
    ) -> pd.DataFrame:
        extractors = get_extractor_order(
            input_feature_list, output_feature_list, self.extractors
        )
        return self._run_extractors(
            extractors, input_df, output_feature_list, timestamps
        )

    def stop(self):
        if self.server is not None:
            self.server.stop(None)
        else:
            raise Exception("Server is not running")

    # ----------------- Private methods -----------------

    def _prepare_extractor_args(
        self, extractor: Extractor, intermediate_data: Dict[str, pd.Series]
    ):
        args = []
        for input in extractor.inputs:
            if isinstance(input, Feature):
                if input.fqn in intermediate_data:
                    args.append(intermediate_data[input.fqn])
                else:
                    raise Exception(
                        f"Feature {input} could not be "
                        f"calculated by any extractor."
                    )
            elif isinstance(input, Featureset):
                series = []
                for feature in input.features:
                    if feature.fqn in intermediate_data:
                        series.append(intermediate_data[feature.fqn])
                    else:
                        raise Exception(
                            f"Feature {feature} couldn't be "
                            f"calculated by any extractor."
                        )
                args.append(pd.concat(series, axis=1))
            else:
                raise Exception(
                    f"Unknown input type {type(input)} found "
                    f"during feature extraction."
                )
        return args

    def _run_extractors(
        self,
        extractors: List[Extractor],
        input_df: pd.DataFrame,
        output_feature_list: List[Union[Feature, Featureset]],
        timestamps: Optional[pd.Series] = None,
    ):
        if timestamps is None:
            timestamps = pd.Series([pd.Timestamp.now()] * len(input_df))
        # Map of feature name to the pandas series
        intermediate_data: Dict[str, pd.Series] = {}
        for col in input_df.columns:
            intermediate_data[col] = input_df[col]
        for extractor in extractors:
            prepare_args = self._prepare_extractor_args(
                extractor, intermediate_data
            )
            output = extractor.func(timestamps, *prepare_args)
            if isinstance(output, pd.Series):
                intermediate_data[output.into_field] = output
            elif isinstance(output, pd.DataFrame):
                for col in output.columns:
                    intermediate_data[col] = output[col]
            else:
                raise Exception(
                    f"Extractor {extractor.name} returned "
                    f"invalid type {type(output)}"
                )

        # Prepare the output dataframe
        output_df = pd.DataFrame()
        for feature in output_feature_list:
            if isinstance(feature, Feature):
                output_df[feature.fqn] = intermediate_data[feature.fqn]
            elif isinstance(feature, Featureset):
                for f in feature.features:
                    output_df[f.fqn] = intermediate_data[f.fqn]
            else:
                raise Exception(
                    f"Unknown feature type {type(feature)} found "
                    f"during feature extraction."
                )
        return output_df

    def _merge_df(self, df: pd.DataFrame, dataset_name: str):
        # Filter the dataframe to only include the columns in the schema
        columns = self.datasets[dataset_name].fields
        input_columns = df.columns.tolist()
        # Check that input columns are a subset of the dataset columns
        if not set(columns).issubset(set(input_columns)):
            raise ValueError(
                f"Dataset columns {columns} are not a subset of "
                f"Input columns {input_columns}"
            )
        df = df[columns]
        if dataset_name not in self.data:
            self.data[dataset_name] = df
        else:
            self.data[dataset_name] = pd.concat([self.data[dataset_name], df])
        # Sort by timestamp
        timestamp_field = self.datasets[dataset_name].timestamp_field
        self.data[dataset_name] = self.data[dataset_name].sort_values(
            timestamp_field
        )


class Servicer(FennelFeatureStoreServicer):
    def Sync(self, request, context):
        pass


def _start_a_test_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_FennelFeatureStoreServicer_to_server(Servicer(), server)
    server.add_insecure_port(f"[::]:{TEST_PORT}")
    server.start()
    return server


def mock_client(test_func):
    def wrapper(*args, **kwargs):
        server = _start_a_test_server()
        with grpc.insecure_channel(f"localhost:{TEST_PORT}") as channel:
            stub = FennelFeatureStoreStub(channel)
            client = MockClient(stub)
            f = test_func(*args, **kwargs, client=client)
            server.stop(0)
            return f

    return wrapper


def create_mock_client():
    server = _start_a_test_server()
    channel = grpc.insecure_channel(f"localhost:{TEST_PORT}")
    stub = FennelFeatureStoreStub(channel)
    client = MockClient(stub, server)
    return client