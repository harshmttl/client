from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from typing import Any, Callable, List, Optional, TypeVar, Union, Tuple, Dict
from typing import Literal
from dataclasses import dataclass

from fennel._vendor.pydantic import BaseModel, Field  # type: ignore
from fennel._vendor.pydantic import validator  # type: ignore
from fennel.connectors.kinesis import at_timestamp
from fennel.internal_lib.duration import (
    Duration,
)
from fennel.internal_lib.duration.duration import is_valid_duration
from fennel.lib.includes import EnvSelector

T = TypeVar("T")
SOURCE_FIELD = "__fennel_data_sources__"
SINK_FIELD = "__fennel_data_sinks__"
DEFAULT_EVERY = Duration("30m")
DEFAULT_DISORDER = Duration("14d")
DEFAULT_WEBHOOK_RETENTION = Duration("7d")
DEFAULT_CDC = "append"


# ------------------------------------------------------------------------------
# source & sink decorators
# ------------------------------------------------------------------------------
class Ref(BaseModel):
    name: str


def ref(ref_name: str) -> PreProcValue:
    return Ref(name=ref_name)


PreProcValue = Union[Ref, Any]


def preproc_has_indirection(preproc: Optional[Dict[str, PreProcValue]]):
    if not preproc:
        return False

    if len(preproc) == 0:
        return False

    for value in preproc.values():
        if isinstance(value, Ref):
            if len(value.name) == 0:
                raise ValueError(
                    "Expected column name to be non empty inside preproc ref type"
                )
            child_names = value.name.split("[")
            # If there is only 1 child, it means there is no indirection
            if len(child_names) == 1:
                return False
            # Last character of all the childs except the first one should be "]"
            for idx in range(1, len(child_names)):
                if child_names[idx][-1] != "]":
                    raise ValueError(
                        "Invalid preproc value of ref type, there is no closing ] for the corresponding opening ["
                    )
            return True
    return False


def source(
    conn: DataConnector,
    disorder: Duration,
    cdc: str,
    every: Optional[Duration] = None,
    since: Optional[datetime] = None,
    until: Optional[datetime] = None,
    env: Optional[Union[str, List[str]]] = None,
    preproc: Optional[Dict[str, PreProcValue]] = None,
    bounded: bool = False,
    idleness: Optional[Duration] = None,
) -> Callable[[T], Any]:
    """
    Decorator to specify the source of data for a dataset. The source can be
    a webhook, a table in a database, a file in S3, a topic in Kafka, etc.
    Refer to https://fennel.ai/docs/api-reference/sources/ for more details.

    :param conn: The external data source to connect to.
    :param disorder: The max out of order delay that can be tolerated.
    :param cdc: The change data capture strategy to use, either "append", "debezium", "upsert" or "native".
    :param every: The frequency at which to fetch data from the source ( Applicable for batch sources only ).
    :param since: The start time from which to fetch data.
    :param until: The end time until which to fetch data.
    :param env: Tier selector to use for the source, for eg "dev", "staging", "prod" etc.
    :param preproc: Preprocessing steps to apply to the data before it is used in the dataset.
    :return:
    """
    if not isinstance(conn, DataConnector):
        if not isinstance(conn, DataSource):
            raise TypeError("Expected a DataSource, found %s" % type(conn))
        raise TypeError(
            f"{conn.name} does not specify required fields "
            f"{', '.join(conn.required_fields())}."
        )

    if (
        isinstance(conn, S3Connector)
        and conn.format == "delta"
        and cdc != "native"
    ):
        raise ValueError("CDC must be set as native for delta format")

    has_preproc_indirection = preproc_has_indirection(preproc)
    if has_preproc_indirection:
        if (
            isinstance(conn, KinesisConnector)
            or isinstance(conn, S3Connector)
            or isinstance(conn, PubSubConnector)
        ) and conn.format != "json":
            raise ValueError(
                "Preproc of type ref('A[B][C]') is applicable only for data in JSON format"
            )
        if (
            isinstance(conn, KafkaConnector)
            and conn.format is not None
            and conn.format != "json"
        ):
            raise ValueError(
                "Preproc of type ref('A[B][C]') is applicable only for data in JSON format"
            )

    if since is not None and not isinstance(since, datetime):
        raise TypeError(f"'since' must be of type datetime - got {type(since)}")

    if until is not None and not isinstance(until, datetime):
        raise TypeError(f"'until' must be of type datetime - got {type(until)}")

    if since is not None and until is not None and since > until:
        raise ValueError(
            f"'since' ({since}) must be earlier than 'until' ({until})"
        )

    if bounded and not idleness:
        raise AttributeError(
            "idleness parameter should always be passed when bounded is set as True"
        )

    if not bounded and idleness:
        raise AttributeError(
            "idleness parameter should not be passed when bounded is set as False"
        )

    def decorator(dataset_cls: T):
        conn.every = every if every is not None else DEFAULT_EVERY
        conn.since = since
        conn.until = until
        conn.disorder = disorder
        conn.cdc = cdc
        conn.envs = EnvSelector(env)
        conn.pre_proc = preproc
        conn.bounded = bounded
        conn.idleness = idleness
        connectors = getattr(dataset_cls, SOURCE_FIELD, [])
        connectors.append(conn)
        setattr(dataset_cls, SOURCE_FIELD, connectors)
        return dataset_cls

    return decorator


def sink(
    conn: DataConnector,
    cdc: str,
    env: Optional[Union[str, List[str]]] = None,
) -> Callable[[T], Any]:
    if not isinstance(conn, DataConnector):
        if not isinstance(conn, DataSource):
            raise TypeError("Expected a DataSource, found %s" % type(conn))
        raise TypeError(
            f"{conn.name} does not specify required fields "
            f"{', '.join(conn.required_fields())}."
        )

    if not isinstance(conn, KafkaConnector):
        raise TypeError(
            "Sink only support Kafka Connector, found %s" % type(conn)
        )

    if cdc != "debezium":
        raise TypeError('Sink only support "debezium" cdc, found %s' % cdc)

    if conn.format != "json":
        raise TypeError(
            'Sink only support "json" format for now, found %s' % cdc
        )

    def decorator(dataset_cls: T):
        conn.cdc = cdc
        conn.envs = EnvSelector(env)
        connectors = getattr(dataset_cls, SINK_FIELD, [])
        connectors.append(conn)
        setattr(dataset_cls, SINK_FIELD, connectors)

        return dataset_cls

    return decorator


# ------------------------------------------------------------------------------
# DataSources
# ------------------------------------------------------------------------------


class DataSource(BaseModel):
    """DataSources are used to define the source of data for a dataset. They
    primarily contain the credentials for the source and can typically contain
    multiple tables/physical datasets. DataSources can also be defined
    through the console and are identified by a unique name."""

    name: str

    def type(self):
        return str(self.__class__.__name__)

    def required_fields(self) -> List[str]:
        raise NotImplementedError()

    def identifier(self) -> str:
        raise NotImplementedError()


class Webhook(DataSource):
    retention: Duration = DEFAULT_WEBHOOK_RETENTION

    @validator("retention")
    def validate_retention(cls, value: Duration) -> str:
        try:
            is_valid_duration(value)
        except Exception as e:
            raise ValueError(
                f"Please provide a valid duration in webhook source: {cls.name}. Error : {e}"
            )
        return value

    def required_fields(self) -> List[str]:
        return ["endpoint"]

    def endpoint(
        self,
        endpoint: str,
    ) -> WebhookConnector:
        return WebhookConnector(self, endpoint)

    def identifier(self) -> str:
        return f"[Webhook: {self.name}]"


class SQLSource(DataSource):
    host: str
    db_name: str
    username: str
    password: str
    jdbc_params: Optional[str] = None
    _get: bool = False

    def required_fields(self) -> List[str]:
        return ["table", "cursor"]


@dataclass
class CSV:
    delimiter: str = ","
    headers: Optional[List[str]] = None


class S3(DataSource):
    aws_access_key_id: Optional[str]
    aws_secret_access_key: Optional[str]
    role_arn: Optional[str]

    def bucket(
        self,
        bucket_name: str,
        prefix: Optional[str] = None,
        path: Optional[str] = None,
        format: str | CSV = CSV(delimiter=",", headers=None),
        presorted: bool = False,
        spread: Optional[Duration] = None,
    ) -> S3Connector:
        return S3Connector(
            self,
            bucket_name,
            prefix,
            path,
            format,
            presorted,
            spread,
        )

    def required_fields(self) -> List[str]:
        return ["bucket"]

    @staticmethod
    def get(name: str) -> S3:
        return S3(
            name=name,
            _get=True,
            aws_access_key_id="",
            aws_secret_access_key="",
            role_arn=None,
        )

    def identifier(self) -> str:
        return f"[S3: {self.name}]"


class BigQuery(DataSource):
    project_id: str
    dataset_id: str
    service_account_key: dict[str, str]

    def table(self, table_name: str, cursor: str) -> TableConnector:
        return TableConnector(self, table_name, cursor)

    def required_fields(self) -> List[str]:
        return ["table", "cursor"]

    @staticmethod
    def get(name: str) -> BigQuery:
        return BigQuery(
            name=name,
            _get=True,
            project_id="",
            dataset_id="",
            service_account_key={},
        )

    def identifier(self) -> str:
        return f"[BigQuery: {self.name}]"


class Avro(BaseModel):
    registry: str
    url: str
    username: Optional[str]
    password: Optional[str]
    token: Optional[str]


class Kafka(DataSource):
    bootstrap_servers: str
    security_protocol: Literal["PLAINTEXT", "SASL_PLAINTEXT", "SASL_SSL"]
    sasl_mechanism: Literal["PLAIN", "SCRAM-SHA-256", "SCRAM-SHA-512", "GSSAPI"]
    sasl_plain_username: Optional[str]
    sasl_plain_password: Optional[str]

    def required_fields(self) -> List[str]:
        return ["topic"]

    def topic(
        self, topic: str, format: Union[str, Avro] = "json"
    ) -> KafkaConnector:
        return KafkaConnector(self, topic, format)

    @staticmethod
    def get(name: str) -> Kafka:
        return Kafka(
            name=name,
            _get=True,
            bootstrap_servers="",
            security_protocol="PLAINTEXT",
            sasl_mechanism="PLAIN",
            sasl_plain_username=None,
            sasl_plain_password=None,
        )

    def identifier(self) -> str:
        return f"[Kafka: {self.name}]"


class Postgres(SQLSource):
    port: int = 5432

    def table(self, table_name: str, cursor: str) -> TableConnector:
        return TableConnector(self, table_name, cursor)

    @staticmethod
    def get(name: str) -> Postgres:
        return Postgres(
            name=name,
            _get=True,
            host="",
            db_name="",
            username="",
            password="",
        )

    def identifier(self) -> str:
        return f"[Postgres: {self.name}]"


class MySQL(SQLSource):
    port: int = 3306

    def table(self, table_name: str, cursor: str) -> TableConnector:
        return TableConnector(self, table_name, cursor)

    @staticmethod
    def get(name: str) -> MySQL:
        return MySQL(
            name=name,
            _get=True,
            host="",
            db_name="",
            username="",
            password="",
        )

    def identifier(self) -> str:
        return f"[MySQL: {self.name}]"


class Snowflake(DataSource):
    account: str
    db_name: str
    username: str
    password: str
    warehouse: str
    src_schema: str = Field(alias="schema")
    role: str

    def table(self, table_name: str, cursor: str) -> TableConnector:
        return TableConnector(self, table_name, cursor)

    def required_fields(self) -> List[str]:
        return ["table", "cursor"]

    @staticmethod
    def get(name: str) -> Snowflake:
        return Snowflake(
            name=name,
            _get=True,
            account="",
            db_name="",
            username="",
            password="",
            warehouse="",
            schema="",
            role="",
        )

    def identifier(self) -> str:
        return f"[Snowflake: {self.name}]"


class Kinesis(DataSource):
    role_arn: str
    _get: bool = False

    def stream(
        self,
        stream_arn: str,
        init_position: str | at_timestamp | datetime | int | float,
        format: str,
    ) -> KinesisConnector:
        return KinesisConnector(self, stream_arn, init_position, format)

    @staticmethod
    def get(name: str) -> Kinesis:
        return Kinesis(
            name=name,
            _get=True,
            role_arn="",
        )

    def identifier(self) -> str:
        return f"[Kinesis: {self.name}]"

    def required_fields(self) -> List[str]:
        return ["role_arn"]


class Redshift(DataSource):
    s3_access_role_arn: str
    db_name: str
    host: str
    port: int = 5439
    src_schema: str = Field(alias="schema")

    def table(self, table_name: str, cursor: str) -> TableConnector:
        return TableConnector(self, table_name, cursor)

    def required_fields(self) -> List[str]:
        return ["table", "cursor"]

    @staticmethod
    def get(name: str) -> Redshift:
        return Redshift(
            name=name,
            _get=True,
            s3_access_role_arn="",
            db_name="",
            host="",
            schema="",
        )

    def identifier(self) -> str:
        return f"[Redshift: {self.name}]"


class Mongo(DataSource):
    host: str
    db_name: str
    username: str
    password: str

    def collection(self, collection_name: str, cursor: str) -> TableConnector:
        return TableConnector(self, table_name=collection_name, cursor=cursor)

    def required_fields(self) -> List[str]:
        return ["table", "cursor"]

    @staticmethod
    def get(name: str) -> Mongo:
        return Mongo(
            name=name,
            _get=True,
            host="",
            db_name="",
            username="",
            password="",
        )

    def identifier(self) -> str:
        return f"[Mongo: {self.name}]"


class PubSub(DataSource):
    project_id: str
    service_account_key: dict[str, str]

    def required_fields(self) -> List[str]:
        return ["topic_id", "format"]

    def topic(self, topic_id: str, format: str) -> PubSubConnector:
        return PubSubConnector(self, topic_id, format)

    @staticmethod
    def get(name: str) -> PubSub:
        return PubSub(
            name=name,
            _get=True,
            project_id="",
            service_account_key={},
        )

    def identifier(self) -> str:
        return f"[PubSub: {self.name}]"


# ------------------------------------------------------------------------------
# DataConnector
# ------------------------------------------------------------------------------
class DataConnector:
    """DataConnector is a fully specified data source or sink. It contains
    all the fields required to fetch data from a source or sink. DataConnectors
    are only created by code and are attached to a dataset."""

    data_source: DataSource
    cdc: str
    every: Optional[Duration] = None
    disorder: Optional[Duration] = None
    since: Optional[datetime] = None
    until: Optional[datetime] = None
    envs: EnvSelector
    pre_proc: Optional[Dict[str, PreProcValue]] = None
    bounded: bool = False
    idleness: Optional[Duration] = None

    def identifier(self):
        raise NotImplementedError


class WebhookConnector(DataConnector):
    """
    Webhook is a DataConnector that is push based rather than pull based.
    This connector enables users to push data directly to fennel either using
    the REST API or the Python SDK.
    """

    endpoint: str

    def __init__(self, source, endpoint):
        self.data_source = source
        self.endpoint = endpoint

    def identifier(self) -> str:
        return f"{self.data_source.identifier()}(endpoint={self.endpoint})"


class TableConnector(DataConnector):
    """DataConnectors which only need a table name and a cursor to be
    specified. Includes BigQuery, MySQL, Postgres, Snowflake and Redshift."""

    table_name: str
    cursor: str

    def __init__(self, source, table_name, cursor):
        self.data_source = source
        self.table_name = table_name
        self.cursor = cursor

    def identifier(self) -> str:
        return f"{self.data_source.identifier()}(table={self.table_name})"


class KafkaConnector(DataConnector):
    """DataConnectors which only need a topic to be specified. Includes
    Kafka."""

    topic: str
    format: Optional[str | Avro]

    def __init__(self, source, topic, format):
        self.data_source = source
        self.topic = topic
        self.format = format

    def identifier(self) -> str:
        return f"{self.data_source.identifier()}(topic={self.topic}, format={self.format})"


class S3Connector(DataConnector):
    bucket_name: Optional[str]
    path_prefix: str
    path_suffix: Optional[str] = None
    delimiter: str = ","
    format: str | CSV = CSV(delimiter=",", headers=None)
    presorted: bool = False
    spread: Optional[Duration] = None

    def __init__(
        self,
        data_source,
        bucket_name,
        path_prefix,
        path,
        format,
        presorted,
        spread,
    ):
        self.data_source = data_source
        self.bucket_name = bucket_name
        self.format = format
        self.presorted = presorted

        if self.format not in [
            "json",
            "parquet",
            "hudi",
            "delta",
        ] and not isinstance(self.format, CSV):
            raise (
                ValueError(
                    "format must be either csv, json, parquet, hudi, delta"
                )
            )

        # Only one of a prefix or path pattern can be specified. If a path is specified,
        # the prefix and suffix are parsed and validated from it
        if path and path_prefix:
            raise AttributeError("path and prefix cannot be specified together")
        elif path_prefix:
            self.path_prefix = path_prefix
        elif path:
            self.path_prefix, self.path_suffix = S3Connector.parse_path(path)
        else:
            raise AttributeError("either path or prefix must be specified")

        if spread:
            if not path:
                raise AttributeError("path must be specified to use spread")
            e = is_valid_duration(spread)
            if e:
                raise ValueError(f"Spread {spread} is an invalid duration: {e}")
            self.spread = spread

    def identifier(self) -> str:
        return (
            f"{self.data_source.identifier()}(bucket={self.bucket_name}"
            f",prefix={self.path_prefix})"
        )

    def creds(self) -> Tuple[Optional[str], Optional[str]]:
        return (
            self.data_source.aws_access_key_id,
            self.data_source.aws_secret_access_key,
        )

    def role_arn(self) -> Optional[str]:
        return self.data_source.role_arn

    @staticmethod
    def parse_path(path: str) -> Tuple[str, str]:
        """Parse a path of form "foo/bar/date=%Y-%m-%d/*" into a prefix and a suffix"""

        ends_with_slash = path.endswith("/")
        # Strip out the ending slash
        if ends_with_slash:
            path = path[:-1]
        parts = path.split("/")
        suffix_portion = False
        prefix = []
        suffix = []
        for i, part in enumerate(parts):
            if part == "*" or part == "**":
                # Wildcard
                suffix_portion = True
                suffix.append(part)
            elif "*" in part:
                # *.file-extension is allowed in the last path part only
                if i != len(parts) - 1:
                    raise ValueError(
                        f"Invalid path part {part}. The * wildcard must be a complete path part except for an ending file extension."
                    )
                pattern = r"^\*\.[a-zA-Z0-9.]+$"
                if not re.match(pattern, part):
                    raise ValueError(
                        f"Invalid path part {part}. The ending path part must be the * wildcard, of the form *.file-extension, a strftime format string, or static string"
                    )
                suffix_portion = True
                suffix.append(part)
            elif "%" in part:
                suffix_portion = True
                # ensure we have a valid strftime format specifier
                try:
                    formatted = datetime.now(timezone.utc).strftime(part)
                    datetime.strptime(formatted, part)
                    suffix.append(part)
                except ValueError:
                    raise ValueError(
                        f"Invalid path part {part}. Invalid datetime format specifier"
                    )
            else:
                pattern = r"^[a-zA-Z0-9._=\-]+$"
                if not re.match(pattern, part):
                    raise ValueError(
                        f"Invalid path part {part}. All path parts must contain alphanumeric characters, hyphens, underscores, dots, `=`, the * or ** wildcards, or strftime format specifiers."
                    )
                # static part. Can be part of prefix until we see a wildcard
                if suffix_portion:
                    suffix.append(part)
                else:
                    prefix.append(part)
        prefix_str, suffix_str = "/".join(prefix), "/".join(suffix)
        # Add the slash to the end of the prefix if it originally had a slash
        if len(prefix_str) > 0 and (len(suffix_str) > 0 or ends_with_slash):
            prefix_str = prefix_str + "/"
        return prefix_str, suffix_str


class KinesisConnector(DataConnector):
    def __init__(
        self,
        data_source,
        stream_arn: str,
        init_position: str | at_timestamp | datetime | int | float,
        format: str,
    ):
        self.data_source = data_source

        if isinstance(init_position, str) and init_position.lower() in [
            "latest",
            "trim_horizon",
        ]:
            # Except for "latest" and "trim_horizon", all other positions are assumed to be timestamps
            self.init_position = init_position.lower()
        elif isinstance(init_position, at_timestamp):
            self.init_position = init_position
        else:
            self.init_position = at_timestamp(init_position)

        if format not in ["json"]:
            raise AttributeError("Kinesis format must be json")
        self.format = format
        self.stream_arn = stream_arn

    stream_arn: str
    init_position: str | at_timestamp
    format: str


class PubSubConnector(DataConnector):
    topic_id: str
    format: str

    def __init__(self, data_source: DataSource, topic_id: str, format: str):
        self.data_source = data_source
        self.topic_id = topic_id
        self.format = format

        if self.format not in ["json"]:
            raise ValueError("format must be json")

    def identifier(self) -> str:
        return f"{self.data_source.identifier()}(topic={self.topic_id}, format={self.format})"
