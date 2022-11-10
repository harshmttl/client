"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import source_pb2
import status_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _AggregateType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _AggregateTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AggregateType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SUM: _AggregateType.ValueType  # 0
    AVG: _AggregateType.ValueType  # 1
    COUNT: _AggregateType.ValueType  # 2
    MIN: _AggregateType.ValueType  # 3
    MAX: _AggregateType.ValueType  # 4
    TOPK: _AggregateType.ValueType  # 5
    CF: _AggregateType.ValueType  # 6

class AggregateType(_AggregateType, metaclass=_AggregateTypeEnumTypeWrapper): ...

SUM: AggregateType.ValueType  # 0
AVG: AggregateType.ValueType  # 1
COUNT: AggregateType.ValueType  # 2
MIN: AggregateType.ValueType  # 3
MAX: AggregateType.ValueType  # 4
TOPK: AggregateType.ValueType  # 5
CF: AggregateType.ValueType  # 6
global___AggregateType = AggregateType

@typing_extensions.final
class Field(google.protobuf.message.Message):
    """All integers representing time are in microseconds and hence should be int64."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    DTYPE_FIELD_NUMBER: builtins.int
    IS_KEY_FIELD_NUMBER: builtins.int
    IS_TIMESTAMP_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    IS_NULLABLE_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    name: builtins.str
    dtype: builtins.bytes
    """Arrow type"""
    is_key: builtins.bool
    is_timestamp: builtins.bool
    owner: builtins.str
    description: builtins.str
    is_nullable: builtins.bool
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        dtype: builtins.bytes = ...,
        is_key: builtins.bool = ...,
        is_timestamp: builtins.bool = ...,
        owner: builtins.str = ...,
        description: builtins.str = ...,
        is_nullable: builtins.bool = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "dtype", b"dtype", "is_key", b"is_key", "is_nullable", b"is_nullable", "is_timestamp", b"is_timestamp", "name", b"name", "owner", b"owner", "tags", b"tags"]) -> None: ...

global___Field = Field

@typing_extensions.final
class PullLookup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FUNCTION_SOURCE_CODE_FIELD_NUMBER: builtins.int
    FUNCTION_FIELD_NUMBER: builtins.int
    function_source_code: builtins.str
    function: builtins.bytes
    def __init__(
        self,
        *,
        function_source_code: builtins.str = ...,
        function: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["function", b"function", "function_source_code", b"function_source_code"]) -> None: ...

global___PullLookup = PullLookup

@typing_extensions.final
class CreateDatasetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    FIELDS_FIELD_NUMBER: builtins.int
    PIPELINES_FIELD_NUMBER: builtins.int
    SOURCES_FIELD_NUMBER: builtins.int
    SINKS_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    RETENTION_FIELD_NUMBER: builtins.int
    MAX_STALENESS_FIELD_NUMBER: builtins.int
    PULL_LOOKUP_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Field]: ...
    @property
    def pipelines(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Pipeline]: ...
    @property
    def sources(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[source_pb2.DataConnector]: ...
    @property
    def sinks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[source_pb2.DataConnector]: ...
    signature: builtins.str
    owner: builtins.str
    description: builtins.str
    mode: builtins.str
    """Default mode is pandas."""
    version: builtins.int
    schema: builtins.bytes
    """Serialized arrow schema."""
    retention: builtins.int
    max_staleness: builtins.int
    @property
    def pull_lookup(self) -> global___PullLookup: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        fields: collections.abc.Iterable[global___Field] | None = ...,
        pipelines: collections.abc.Iterable[global___Pipeline] | None = ...,
        sources: collections.abc.Iterable[source_pb2.DataConnector] | None = ...,
        sinks: collections.abc.Iterable[source_pb2.DataConnector] | None = ...,
        signature: builtins.str = ...,
        owner: builtins.str = ...,
        description: builtins.str = ...,
        mode: builtins.str = ...,
        version: builtins.int = ...,
        schema: builtins.bytes = ...,
        retention: builtins.int = ...,
        max_staleness: builtins.int = ...,
        pull_lookup: global___PullLookup | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pull_lookup", b"pull_lookup"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "fields", b"fields", "max_staleness", b"max_staleness", "mode", b"mode", "name", b"name", "owner", b"owner", "pipelines", b"pipelines", "pull_lookup", b"pull_lookup", "retention", b"retention", "schema", b"schema", "signature", b"signature", "sinks", b"sinks", "sources", b"sources", "version", b"version"]) -> None: ...

global___CreateDatasetRequest = CreateDatasetRequest

@typing_extensions.final
class CreateDatasetResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def status(self) -> status_pb2.Status: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        status: status_pb2.Status | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "status", b"status"]) -> None: ...

global___CreateDatasetResponse = CreateDatasetResponse

@typing_extensions.final
class Pipeline(google.protobuf.message.Message):
    """----------------------------------------------------------------------------------------------
    Pipeline
    ----------------------------------------------------------------------------------------------
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODES_FIELD_NUMBER: builtins.int
    ROOT_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    INPUTS_FIELD_NUMBER: builtins.int
    @property
    def nodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Node]:
        """Nodes in the pipeline."""
    root: builtins.str
    """Id of the root node."""
    signature: builtins.str
    @property
    def inputs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of input datasets."""
    def __init__(
        self,
        *,
        nodes: collections.abc.Iterable[global___Node] | None = ...,
        root: builtins.str = ...,
        signature: builtins.str = ...,
        inputs: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["inputs", b"inputs", "nodes", b"nodes", "root", b"root", "signature", b"signature"]) -> None: ...

global___Pipeline = Pipeline

@typing_extensions.final
class Node(google.protobuf.message.Message):
    """Each Node in the pipeline either refers to a dataset or an operator.
    Each node also has a globally unique id. Operators refer to their inputs via
    their corresponding node ids.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    OPERATOR_FIELD_NUMBER: builtins.int
    DATASET_NAME_FIELD_NUMBER: builtins.int
    id: builtins.str
    @property
    def operator(self) -> global___Operator: ...
    dataset_name: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        operator: global___Operator | None = ...,
        dataset_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dataset_name", b"dataset_name", "node", b"node", "operator", b"operator"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset_name", b"dataset_name", "id", b"id", "node", b"node", "operator", b"operator"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["node", b"node"]) -> typing_extensions.Literal["operator", "dataset_name"] | None: ...

global___Node = Node

@typing_extensions.final
class Operator(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AGGREGATE_FIELD_NUMBER: builtins.int
    JOIN_FIELD_NUMBER: builtins.int
    TRANSFORM_FIELD_NUMBER: builtins.int
    UNION_FIELD_NUMBER: builtins.int
    @property
    def aggregate(self) -> global___Aggregate: ...
    @property
    def join(self) -> global___Join: ...
    @property
    def transform(self) -> global___Transform: ...
    @property
    def union(self) -> global___Union: ...
    def __init__(
        self,
        *,
        aggregate: global___Aggregate | None = ...,
        join: global___Join | None = ...,
        transform: global___Transform | None = ...,
        union: global___Union | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["aggregate", b"aggregate", "join", b"join", "op", b"op", "transform", b"transform", "union", b"union"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["aggregate", b"aggregate", "join", b"join", "op", b"op", "transform", b"transform", "union", b"union"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["op", b"op"]) -> typing_extensions.Literal["aggregate", "join", "transform", "union"] | None: ...

global___Operator = Operator

@typing_extensions.final
class Aggregate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_NODE_ID_FIELD_NUMBER: builtins.int
    KEYS_FIELD_NUMBER: builtins.int
    AGGREGATES_FIELD_NUMBER: builtins.int
    operand_node_id: builtins.str
    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def aggregates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Aggregation]: ...
    def __init__(
        self,
        *,
        operand_node_id: builtins.str = ...,
        keys: collections.abc.Iterable[builtins.str] | None = ...,
        aggregates: collections.abc.Iterable[global___Aggregation] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aggregates", b"aggregates", "keys", b"keys", "operand_node_id", b"operand_node_id"]) -> None: ...

global___Aggregate = Aggregate

@typing_extensions.final
class Join(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class OnEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    LHS_NODE_ID_FIELD_NUMBER: builtins.int
    RHS_DATASET_NAME_FIELD_NUMBER: builtins.int
    ON_FIELD_NUMBER: builtins.int
    lhs_node_id: builtins.str
    rhs_dataset_name: builtins.str
    """RHS of a JOIN can only be a dataset."""
    @property
    def on(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Map of left field name to right field name to join on."""
    def __init__(
        self,
        *,
        lhs_node_id: builtins.str = ...,
        rhs_dataset_name: builtins.str = ...,
        on: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["lhs_node_id", b"lhs_node_id", "on", b"on", "rhs_dataset_name", b"rhs_dataset_name"]) -> None: ...

global___Join = Join

@typing_extensions.final
class Transform(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_NODE_ID_FIELD_NUMBER: builtins.int
    FUNCTION_FIELD_NUMBER: builtins.int
    FUNCTION_SOURCE_CODE_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_FIELD_NUMBER: builtins.int
    operand_node_id: builtins.str
    function: builtins.bytes
    function_source_code: builtins.str
    timestamp_field: builtins.str
    def __init__(
        self,
        *,
        operand_node_id: builtins.str = ...,
        function: builtins.bytes = ...,
        function_source_code: builtins.str = ...,
        timestamp_field: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["function", b"function", "function_source_code", b"function_source_code", "operand_node_id", b"operand_node_id", "timestamp_field", b"timestamp_field"]) -> None: ...

global___Transform = Transform

@typing_extensions.final
class Union(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERAND_NODE_IDS_FIELD_NUMBER: builtins.int
    @property
    def operand_node_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        operand_node_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["operand_node_ids", b"operand_node_ids"]) -> None: ...

global___Union = Union

@typing_extensions.final
class Aggregation(google.protobuf.message.Message):
    """----------------------------------------------------------------------------
    Aggregate Definitions
    ----------------------------------------------------------------------------
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    WINDOW_SPEC_FIELD_NUMBER: builtins.int
    VALUE_FIELD_FIELD_NUMBER: builtins.int
    TOPK_FIELD_NUMBER: builtins.int
    CF_FIELD_NUMBER: builtins.int
    type: global___AggregateType.ValueType
    @property
    def window_spec(self) -> global___WindowSpec: ...
    value_field: builtins.str
    @property
    def topk(self) -> global___TopKConfig: ...
    @property
    def cf(self) -> global___CFConfig: ...
    def __init__(
        self,
        *,
        type: global___AggregateType.ValueType = ...,
        window_spec: global___WindowSpec | None = ...,
        value_field: builtins.str = ...,
        topk: global___TopKConfig | None = ...,
        cf: global___CFConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cf", b"cf", "config", b"config", "topk", b"topk", "value_field", b"value_field", "window_spec", b"window_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cf", b"cf", "config", b"config", "topk", b"topk", "type", b"type", "value_field", b"value_field", "window_spec", b"window_spec"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["config", b"config"]) -> typing_extensions.Literal["value_field", "topk", "cf"] | None: ...

global___Aggregation = Aggregation

@typing_extensions.final
class Window(google.protobuf.message.Message):
    """to = 0 represents last X window."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_FIELD_NUMBER: builtins.int
    END_FIELD_NUMBER: builtins.int
    start: builtins.int
    end: builtins.int
    def __init__(
        self,
        *,
        start: builtins.int = ...,
        end: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["end", b"end", "start", b"start"]) -> None: ...

global___Window = Window

@typing_extensions.final
class DeltaWindow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASELINE_FIELD_NUMBER: builtins.int
    TARGET_FIELD_NUMBER: builtins.int
    @property
    def baseline(self) -> global___Window: ...
    @property
    def target(self) -> global___Window: ...
    def __init__(
        self,
        *,
        baseline: global___Window | None = ...,
        target: global___Window | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["baseline", b"baseline", "target", b"target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["baseline", b"baseline", "target", b"target"]) -> None: ...

global___DeltaWindow = DeltaWindow

@typing_extensions.final
class WindowSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOREVER_WINDOW_FIELD_NUMBER: builtins.int
    WINDOW_FIELD_NUMBER: builtins.int
    DELTA_WINDOW_FIELD_NUMBER: builtins.int
    forever_window: builtins.bool
    @property
    def window(self) -> global___Window: ...
    @property
    def delta_window(self) -> global___DeltaWindow: ...
    def __init__(
        self,
        *,
        forever_window: builtins.bool = ...,
        window: global___Window | None = ...,
        delta_window: global___DeltaWindow | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["delta_window", b"delta_window", "forever_window", b"forever_window", "spec", b"spec", "window", b"window"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delta_window", b"delta_window", "forever_window", b"forever_window", "spec", b"spec", "window", b"window"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["spec", b"spec"]) -> typing_extensions.Literal["forever_window", "window", "delta_window"] | None: ...

global___WindowSpec = WindowSpec

@typing_extensions.final
class TopKConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    K_FIELD_NUMBER: builtins.int
    ITEM_FIELDS_FIELD_NUMBER: builtins.int
    SCORE_FIELD_FIELD_NUMBER: builtins.int
    k: builtins.int
    @property
    def item_fields(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    score_field: builtins.str
    def __init__(
        self,
        *,
        k: builtins.int = ...,
        item_fields: collections.abc.Iterable[builtins.str] | None = ...,
        score_field: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["item_fields", b"item_fields", "k", b"k", "score_field", b"score_field"]) -> None: ...

global___TopKConfig = TopKConfig

@typing_extensions.final
class CFConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIMIT_FIELD_NUMBER: builtins.int
    CONTEXT_FIELDS_FIELD_NUMBER: builtins.int
    WEIGHT_FIELD_FIELD_NUMBER: builtins.int
    limit: builtins.int
    @property
    def context_fields(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    weight_field: builtins.str
    def __init__(
        self,
        *,
        limit: builtins.int = ...,
        context_fields: collections.abc.Iterable[builtins.str] | None = ...,
        weight_field: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["context_fields", b"context_fields", "limit", b"limit", "weight_field", b"weight_field"]) -> None: ...

global___CFConfig = CFConfig
