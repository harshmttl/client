"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
proto2 vs proto3 -
https://github.com/protocolbuffers/protobuf/releases/tag/v3.0.0
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class DataConnector(google.protobuf.message.Message):
    """Next field number: 6"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_FIELD_NUMBER: builtins.int
    CURSOR_FIELD_NUMBER: builtins.int
    TABLE_FIELD_NUMBER: builtins.int
    S3_CONNECTOR_FIELD_NUMBER: builtins.int
    EVERY_FIELD_NUMBER: builtins.int
    @property
    def source(self) -> global___DataSource: ...
    cursor: builtins.str
    table: builtins.str
    @property
    def s3_connector(self) -> global___S3Connector: ...
    every: builtins.int
    def __init__(
        self,
        *,
        source: global___DataSource | None = ...,
        cursor: builtins.str = ...,
        table: builtins.str = ...,
        s3_connector: global___S3Connector | None = ...,
        every: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["instance", b"instance", "s3_connector", b"s3_connector", "source", b"source", "table", b"table"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cursor", b"cursor", "every", b"every", "instance", b"instance", "s3_connector", b"s3_connector", "source", b"source", "table", b"table"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["instance", b"instance"]) -> typing_extensions.Literal["table", "s3_connector"] | None: ...

global___DataConnector = DataConnector

class DataSource(google.protobuf.message.Message):
    """Next field number: 6"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    SQL_FIELD_NUMBER: builtins.int
    S3_FIELD_NUMBER: builtins.int
    BIGQUERY_FIELD_NUMBER: builtins.int
    SNOWFLAKE_FIELD_NUMBER: builtins.int
    EXISTING_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def sql(self) -> global___SQL: ...
    @property
    def s3(self) -> global___S3: ...
    @property
    def bigquery(self) -> global___BigQuery: ...
    @property
    def snowflake(self) -> global___Snowflake: ...
    existing: builtins.bool
    """When a source has already been created on the console
    Or via code and is specified by name ONLY.
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        sql: global___SQL | None = ...,
        s3: global___S3 | None = ...,
        bigquery: global___BigQuery | None = ...,
        snowflake: global___Snowflake | None = ...,
        existing: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bigquery", b"bigquery", "existing", b"existing", "s3", b"s3", "snowflake", b"snowflake", "source", b"source", "sql", b"sql"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bigquery", b"bigquery", "existing", b"existing", "name", b"name", "s3", b"s3", "snowflake", b"snowflake", "source", b"source", "sql", b"sql"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["source", b"source"]) -> typing_extensions.Literal["sql", "s3", "bigquery", "snowflake", "existing"] | None: ...

global___DataSource = DataSource

class SQL(google.protobuf.message.Message):
    """Next field number: 8"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _SQLType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _SQLTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SQL._SQLType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Postgres: SQL._SQLType.ValueType  # 0
        MySQL: SQL._SQLType.ValueType  # 1

    class SQLType(_SQLType, metaclass=_SQLTypeEnumTypeWrapper): ...
    Postgres: SQL.SQLType.ValueType  # 0
    MySQL: SQL.SQLType.ValueType  # 1

    SQL_TYPE_FIELD_NUMBER: builtins.int
    HOST_FIELD_NUMBER: builtins.int
    DB_FIELD_NUMBER: builtins.int
    USERNAME_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    JDBC_PARAMS_FIELD_NUMBER: builtins.int
    sql_type: global___SQL.SQLType.ValueType
    host: builtins.str
    db: builtins.str
    username: builtins.str
    password: builtins.str
    port: builtins.int
    jdbc_params: builtins.str
    def __init__(
        self,
        *,
        sql_type: global___SQL.SQLType.ValueType = ...,
        host: builtins.str = ...,
        db: builtins.str = ...,
        username: builtins.str = ...,
        password: builtins.str = ...,
        port: builtins.int = ...,
        jdbc_params: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["db", b"db", "host", b"host", "jdbc_params", b"jdbc_params", "password", b"password", "port", b"port", "sql_type", b"sql_type", "username", b"username"]) -> None: ...

global___SQL = SQL

class S3(google.protobuf.message.Message):
    """Next field number: 6"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AWS_ACCESS_KEY_ID_FIELD_NUMBER: builtins.int
    AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: builtins.int
    aws_access_key_id: builtins.str
    aws_secret_access_key: builtins.str
    def __init__(
        self,
        *,
        aws_access_key_id: builtins.str = ...,
        aws_secret_access_key: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aws_access_key_id", b"aws_access_key_id", "aws_secret_access_key", b"aws_secret_access_key"]) -> None: ...

global___S3 = S3

class S3Connector(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class SchemaEntry(google.protobuf.message.Message):
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

    BUCKET_FIELD_NUMBER: builtins.int
    PATH_PREFIX_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    DELIMITER_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    bucket: builtins.str
    path_prefix: builtins.str
    @property
    def schema(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    delimiter: builtins.str
    format: builtins.str
    def __init__(
        self,
        *,
        bucket: builtins.str = ...,
        path_prefix: builtins.str = ...,
        schema: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        delimiter: builtins.str = ...,
        format: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bucket", b"bucket", "delimiter", b"delimiter", "format", b"format", "path_prefix", b"path_prefix", "schema", b"schema"]) -> None: ...

global___S3Connector = S3Connector

class BigQuery(google.protobuf.message.Message):
    """Next field number: 4"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    DATASET_FIELD_NUMBER: builtins.int
    CREDENTIALS_JSON_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    dataset: builtins.str
    credentials_json: builtins.str
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        dataset: builtins.str = ...,
        credentials_json: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["credentials_json", b"credentials_json", "dataset", b"dataset", "project_id", b"project_id"]) -> None: ...

global___BigQuery = BigQuery

class Snowflake(google.protobuf.message.Message):
    """Next field number: 9"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_FIELD_NUMBER: builtins.int
    USERNAME_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    DB_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    WAREHOUSE_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    JDBC_PARAMS_FIELD_NUMBER: builtins.int
    account: builtins.str
    username: builtins.str
    password: builtins.str
    db: builtins.str
    schema: builtins.str
    warehouse: builtins.str
    role: builtins.str
    jdbc_params: builtins.str
    def __init__(
        self,
        *,
        account: builtins.str = ...,
        username: builtins.str = ...,
        password: builtins.str = ...,
        db: builtins.str = ...,
        schema: builtins.str = ...,
        warehouse: builtins.str = ...,
        role: builtins.str = ...,
        jdbc_params: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account", b"account", "db", b"db", "jdbc_params", b"jdbc_params", "password", b"password", "role", b"role", "schema", b"schema", "username", b"username", "warehouse", b"warehouse"]) -> None: ...

global___Snowflake = Snowflake
