"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

Vocabulary:
1. ExtDatabase refers to DB in external data sources & contains
credentials/config.
2. ExtTable refers to a specific table etc. in the context of an external
database
3. Source refers to a (table, dataset) along with some config
4. Sink refers to a (table, dataset) along with some config
5. This whole module is called connector.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import kinesis_pb2
import schema_pb2
import schema_registry_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _CDCStrategy:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CDCStrategyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CDCStrategy.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    Append: _CDCStrategy.ValueType  # 0
    Upsert: _CDCStrategy.ValueType  # 1
    Debezium: _CDCStrategy.ValueType  # 2
    Native: _CDCStrategy.ValueType  # 3
    Delete: _CDCStrategy.ValueType  # 4

class CDCStrategy(_CDCStrategy, metaclass=_CDCStrategyEnumTypeWrapper): ...

Append: CDCStrategy.ValueType  # 0
Upsert: CDCStrategy.ValueType  # 1
Debezium: CDCStrategy.ValueType  # 2
Native: CDCStrategy.ValueType  # 3
Delete: CDCStrategy.ValueType  # 4
global___CDCStrategy = CDCStrategy

@typing_extensions.final
class ExtDatabase(google.protobuf.message.Message):
    """-----------------------------------------
    First we have all the databases
    -----------------------------------------
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    MYSQL_FIELD_NUMBER: builtins.int
    POSTGRES_FIELD_NUMBER: builtins.int
    REFERENCE_FIELD_NUMBER: builtins.int
    S3_FIELD_NUMBER: builtins.int
    BIGQUERY_FIELD_NUMBER: builtins.int
    SNOWFLAKE_FIELD_NUMBER: builtins.int
    KAFKA_FIELD_NUMBER: builtins.int
    WEBHOOK_FIELD_NUMBER: builtins.int
    KINESIS_FIELD_NUMBER: builtins.int
    REDSHIFT_FIELD_NUMBER: builtins.int
    MONGO_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def mysql(self) -> global___MySQL: ...
    @property
    def postgres(self) -> global___Postgres: ...
    @property
    def reference(self) -> global___Reference:
        """When a source has already been created on the console
        Or via code and is specified by name ONLY.
        """
    @property
    def s3(self) -> global___S3: ...
    @property
    def bigquery(self) -> global___Bigquery: ...
    @property
    def snowflake(self) -> global___Snowflake: ...
    @property
    def kafka(self) -> global___Kafka: ...
    @property
    def webhook(self) -> global___Webhook: ...
    @property
    def kinesis(self) -> global___Kinesis: ...
    @property
    def redshift(self) -> global___Redshift: ...
    @property
    def mongo(self) -> global___Mongo: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        mysql: global___MySQL | None = ...,
        postgres: global___Postgres | None = ...,
        reference: global___Reference | None = ...,
        s3: global___S3 | None = ...,
        bigquery: global___Bigquery | None = ...,
        snowflake: global___Snowflake | None = ...,
        kafka: global___Kafka | None = ...,
        webhook: global___Webhook | None = ...,
        kinesis: global___Kinesis | None = ...,
        redshift: global___Redshift | None = ...,
        mongo: global___Mongo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bigquery", b"bigquery", "kafka", b"kafka", "kinesis", b"kinesis", "mongo", b"mongo", "mysql", b"mysql", "postgres", b"postgres", "redshift", b"redshift", "reference", b"reference", "s3", b"s3", "snowflake", b"snowflake", "variant", b"variant", "webhook", b"webhook"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bigquery", b"bigquery", "kafka", b"kafka", "kinesis", b"kinesis", "mongo", b"mongo", "mysql", b"mysql", "name", b"name", "postgres", b"postgres", "redshift", b"redshift", "reference", b"reference", "s3", b"s3", "snowflake", b"snowflake", "variant", b"variant", "webhook", b"webhook"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["variant", b"variant"]) -> typing_extensions.Literal["mysql", "postgres", "reference", "s3", "bigquery", "snowflake", "kafka", "webhook", "kinesis", "redshift", "mongo"] | None: ...

global___ExtDatabase = ExtDatabase

@typing_extensions.final
class KafkaFormat(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JSON_FIELD_NUMBER: builtins.int
    AVRO_FIELD_NUMBER: builtins.int
    @property
    def json(self) -> global___JsonFormat: ...
    @property
    def avro(self) -> global___AvroFormat: ...
    def __init__(
        self,
        *,
        json: global___JsonFormat | None = ...,
        avro: global___AvroFormat | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["avro", b"avro", "json", b"json", "variant", b"variant"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["avro", b"avro", "json", b"json", "variant", b"variant"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["variant", b"variant"]) -> typing_extensions.Literal["json", "avro"] | None: ...

global___KafkaFormat = KafkaFormat

@typing_extensions.final
class JsonFormat(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___JsonFormat = JsonFormat

@typing_extensions.final
class AvroFormat(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCHEMA_REGISTRY_FIELD_NUMBER: builtins.int
    @property
    def schema_registry(self) -> schema_registry_pb2.SchemaRegistry: ...
    def __init__(
        self,
        *,
        schema_registry: schema_registry_pb2.SchemaRegistry | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["schema_registry", b"schema_registry"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["schema_registry", b"schema_registry"]) -> None: ...

global___AvroFormat = AvroFormat

@typing_extensions.final
class Reference(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ExtDBType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ExtDBTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Reference._ExtDBType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        MYSQL: Reference._ExtDBType.ValueType  # 0
        POSTGRES: Reference._ExtDBType.ValueType  # 1
        S3: Reference._ExtDBType.ValueType  # 2
        KAFKA: Reference._ExtDBType.ValueType  # 3
        BIGQUERY: Reference._ExtDBType.ValueType  # 4
        SNOWFLAKE: Reference._ExtDBType.ValueType  # 5
        WEBHOOK: Reference._ExtDBType.ValueType  # 6
        KINESIS: Reference._ExtDBType.ValueType  # 7
        REDSHIFT: Reference._ExtDBType.ValueType  # 8
        MONGO: Reference._ExtDBType.ValueType  # 9

    class ExtDBType(_ExtDBType, metaclass=_ExtDBTypeEnumTypeWrapper): ...
    MYSQL: Reference.ExtDBType.ValueType  # 0
    POSTGRES: Reference.ExtDBType.ValueType  # 1
    S3: Reference.ExtDBType.ValueType  # 2
    KAFKA: Reference.ExtDBType.ValueType  # 3
    BIGQUERY: Reference.ExtDBType.ValueType  # 4
    SNOWFLAKE: Reference.ExtDBType.ValueType  # 5
    WEBHOOK: Reference.ExtDBType.ValueType  # 6
    KINESIS: Reference.ExtDBType.ValueType  # 7
    REDSHIFT: Reference.ExtDBType.ValueType  # 8
    MONGO: Reference.ExtDBType.ValueType  # 9

    DBTYPE_FIELD_NUMBER: builtins.int
    dbtype: global___Reference.ExtDBType.ValueType
    def __init__(
        self,
        *,
        dbtype: global___Reference.ExtDBType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dbtype", b"dbtype"]) -> None: ...

global___Reference = Reference

@typing_extensions.final
class Webhook(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    RETENTION_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def retention(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        retention: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["retention", b"retention"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "retention", b"retention"]) -> None: ...

global___Webhook = Webhook

@typing_extensions.final
class MySQL(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    JDBC_PARAMS_FIELD_NUMBER: builtins.int
    host: builtins.str
    database: builtins.str
    user: builtins.str
    password: builtins.str
    port: builtins.int
    jdbc_params: builtins.str
    def __init__(
        self,
        *,
        host: builtins.str = ...,
        database: builtins.str = ...,
        user: builtins.str = ...,
        password: builtins.str = ...,
        port: builtins.int = ...,
        jdbc_params: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database", b"database", "host", b"host", "jdbc_params", b"jdbc_params", "password", b"password", "port", b"port", "user", b"user"]) -> None: ...

global___MySQL = MySQL

@typing_extensions.final
class Postgres(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    JDBC_PARAMS_FIELD_NUMBER: builtins.int
    host: builtins.str
    database: builtins.str
    user: builtins.str
    password: builtins.str
    port: builtins.int
    jdbc_params: builtins.str
    def __init__(
        self,
        *,
        host: builtins.str = ...,
        database: builtins.str = ...,
        user: builtins.str = ...,
        password: builtins.str = ...,
        port: builtins.int = ...,
        jdbc_params: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database", b"database", "host", b"host", "jdbc_params", b"jdbc_params", "password", b"password", "port", b"port", "user", b"user"]) -> None: ...

global___Postgres = Postgres

@typing_extensions.final
class S3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: builtins.int
    AWS_ACCESS_KEY_ID_FIELD_NUMBER: builtins.int
    aws_secret_access_key: builtins.str
    aws_access_key_id: builtins.str
    def __init__(
        self,
        *,
        aws_secret_access_key: builtins.str = ...,
        aws_access_key_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aws_access_key_id", b"aws_access_key_id", "aws_secret_access_key", b"aws_secret_access_key"]) -> None: ...

global___S3 = S3

@typing_extensions.final
class Bigquery(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATASET_ID_FIELD_NUMBER: builtins.int
    CREDENTIALS_JSON_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    dataset_id: builtins.str
    credentials_json: builtins.str
    project_id: builtins.str
    def __init__(
        self,
        *,
        dataset_id: builtins.str = ...,
        credentials_json: builtins.str = ...,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["credentials_json", b"credentials_json", "dataset_id", b"dataset_id", "project_id", b"project_id"]) -> None: ...

global___Bigquery = Bigquery

@typing_extensions.final
class Snowflake(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    WAREHOUSE_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    account: builtins.str
    user: builtins.str
    password: builtins.str
    schema: builtins.str
    warehouse: builtins.str
    role: builtins.str
    database: builtins.str
    def __init__(
        self,
        *,
        account: builtins.str = ...,
        user: builtins.str = ...,
        password: builtins.str = ...,
        schema: builtins.str = ...,
        warehouse: builtins.str = ...,
        role: builtins.str = ...,
        database: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account", b"account", "database", b"database", "password", b"password", "role", b"role", "schema", b"schema", "user", b"user", "warehouse", b"warehouse"]) -> None: ...

global___Snowflake = Snowflake

@typing_extensions.final
class Kafka(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BOOTSTRAP_SERVERS_FIELD_NUMBER: builtins.int
    SECURITY_PROTOCOL_FIELD_NUMBER: builtins.int
    SASL_MECHANISM_FIELD_NUMBER: builtins.int
    SASL_JAAS_CONFIG_FIELD_NUMBER: builtins.int
    SASL_PLAIN_USERNAME_FIELD_NUMBER: builtins.int
    SASL_PLAIN_PASSWORD_FIELD_NUMBER: builtins.int
    GROUP_ID_FIELD_NUMBER: builtins.int
    bootstrap_servers: builtins.str
    security_protocol: builtins.str
    sasl_mechanism: builtins.str
    sasl_jaas_config: builtins.str
    sasl_plain_username: builtins.str
    sasl_plain_password: builtins.str
    group_id: builtins.str
    def __init__(
        self,
        *,
        bootstrap_servers: builtins.str = ...,
        security_protocol: builtins.str = ...,
        sasl_mechanism: builtins.str = ...,
        sasl_jaas_config: builtins.str = ...,
        sasl_plain_username: builtins.str = ...,
        sasl_plain_password: builtins.str = ...,
        group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bootstrap_servers", b"bootstrap_servers", "group_id", b"group_id", "sasl_jaas_config", b"sasl_jaas_config", "sasl_mechanism", b"sasl_mechanism", "sasl_plain_password", b"sasl_plain_password", "sasl_plain_username", b"sasl_plain_username", "security_protocol", b"security_protocol"]) -> None: ...

global___Kafka = Kafka

@typing_extensions.final
class Kinesis(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLE_ARN_FIELD_NUMBER: builtins.int
    role_arn: builtins.str
    def __init__(
        self,
        *,
        role_arn: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["role_arn", b"role_arn"]) -> None: ...

global___Kinesis = Kinesis

@typing_extensions.final
class Redshift(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    S3_ACCESS_ROLE_ARN_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    HOST_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    s3_access_role_arn: builtins.str
    database: builtins.str
    host: builtins.str
    port: builtins.int
    def __init__(
        self,
        *,
        s3_access_role_arn: builtins.str = ...,
        database: builtins.str = ...,
        host: builtins.str = ...,
        port: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database", b"database", "host", b"host", "port", b"port", "s3_access_role_arn", b"s3_access_role_arn"]) -> None: ...

global___Redshift = Redshift

@typing_extensions.final
class Mongo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    host: builtins.str
    database: builtins.str
    user: builtins.str
    password: builtins.str
    def __init__(
        self,
        *,
        host: builtins.str = ...,
        database: builtins.str = ...,
        user: builtins.str = ...,
        password: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database", b"database", "host", b"host", "password", b"password", "user", b"user"]) -> None: ...

global___Mongo = Mongo

@typing_extensions.final
class ExtTable(google.protobuf.message.Message):
    """-----------------------------------------
    Next, all the tables
    -----------------------------------------
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MYSQL_TABLE_FIELD_NUMBER: builtins.int
    PG_TABLE_FIELD_NUMBER: builtins.int
    S3_TABLE_FIELD_NUMBER: builtins.int
    KAFKA_TOPIC_FIELD_NUMBER: builtins.int
    SNOWFLAKE_TABLE_FIELD_NUMBER: builtins.int
    BIGQUERY_TABLE_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    KINESIS_STREAM_FIELD_NUMBER: builtins.int
    REDSHIFT_TABLE_FIELD_NUMBER: builtins.int
    MONGO_COLLECTION_FIELD_NUMBER: builtins.int
    @property
    def mysql_table(self) -> global___MySQLTable: ...
    @property
    def pg_table(self) -> global___PostgresTable: ...
    @property
    def s3_table(self) -> global___S3Table: ...
    @property
    def kafka_topic(self) -> global___KafkaTopic: ...
    @property
    def snowflake_table(self) -> global___SnowflakeTable: ...
    @property
    def bigquery_table(self) -> global___BigqueryTable: ...
    @property
    def endpoint(self) -> global___WebhookEndpoint: ...
    @property
    def kinesis_stream(self) -> global___KinesisStream: ...
    @property
    def redshift_table(self) -> global___RedshiftTable: ...
    @property
    def mongo_collection(self) -> global___MongoCollection: ...
    def __init__(
        self,
        *,
        mysql_table: global___MySQLTable | None = ...,
        pg_table: global___PostgresTable | None = ...,
        s3_table: global___S3Table | None = ...,
        kafka_topic: global___KafkaTopic | None = ...,
        snowflake_table: global___SnowflakeTable | None = ...,
        bigquery_table: global___BigqueryTable | None = ...,
        endpoint: global___WebhookEndpoint | None = ...,
        kinesis_stream: global___KinesisStream | None = ...,
        redshift_table: global___RedshiftTable | None = ...,
        mongo_collection: global___MongoCollection | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bigquery_table", b"bigquery_table", "endpoint", b"endpoint", "kafka_topic", b"kafka_topic", "kinesis_stream", b"kinesis_stream", "mongo_collection", b"mongo_collection", "mysql_table", b"mysql_table", "pg_table", b"pg_table", "redshift_table", b"redshift_table", "s3_table", b"s3_table", "snowflake_table", b"snowflake_table", "variant", b"variant"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bigquery_table", b"bigquery_table", "endpoint", b"endpoint", "kafka_topic", b"kafka_topic", "kinesis_stream", b"kinesis_stream", "mongo_collection", b"mongo_collection", "mysql_table", b"mysql_table", "pg_table", b"pg_table", "redshift_table", b"redshift_table", "s3_table", b"s3_table", "snowflake_table", b"snowflake_table", "variant", b"variant"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["variant", b"variant"]) -> typing_extensions.Literal["mysql_table", "pg_table", "s3_table", "kafka_topic", "snowflake_table", "bigquery_table", "endpoint", "kinesis_stream", "redshift_table", "mongo_collection"] | None: ...

global___ExtTable = ExtTable

@typing_extensions.final
class MySQLTable(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    @property
    def db(self) -> global___ExtDatabase: ...
    table_name: builtins.str
    def __init__(
        self,
        *,
        db: global___ExtDatabase | None = ...,
        table_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["db", b"db"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["db", b"db", "table_name", b"table_name"]) -> None: ...

global___MySQLTable = MySQLTable

@typing_extensions.final
class PostgresTable(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    @property
    def db(self) -> global___ExtDatabase: ...
    table_name: builtins.str
    def __init__(
        self,
        *,
        db: global___ExtDatabase | None = ...,
        table_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["db", b"db"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["db", b"db", "table_name", b"table_name"]) -> None: ...

global___PostgresTable = PostgresTable

@typing_extensions.final
class S3Table(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUCKET_FIELD_NUMBER: builtins.int
    PATH_PREFIX_FIELD_NUMBER: builtins.int
    DELIMITER_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    DB_FIELD_NUMBER: builtins.int
    PRE_SORTED_FIELD_NUMBER: builtins.int
    PATH_SUFFIX_FIELD_NUMBER: builtins.int
    SPREAD_FIELD_NUMBER: builtins.int
    bucket: builtins.str
    path_prefix: builtins.str
    delimiter: builtins.str
    format: builtins.str
    @property
    def db(self) -> global___ExtDatabase: ...
    pre_sorted: builtins.bool
    path_suffix: builtins.str
    @property
    def spread(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        bucket: builtins.str = ...,
        path_prefix: builtins.str = ...,
        delimiter: builtins.str = ...,
        format: builtins.str = ...,
        db: global___ExtDatabase | None = ...,
        pre_sorted: builtins.bool = ...,
        path_suffix: builtins.str = ...,
        spread: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_spread", b"_spread", "db", b"db", "spread", b"spread"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_spread", b"_spread", "bucket", b"bucket", "db", b"db", "delimiter", b"delimiter", "format", b"format", "path_prefix", b"path_prefix", "path_suffix", b"path_suffix", "pre_sorted", b"pre_sorted", "spread", b"spread"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_spread", b"_spread"]) -> typing_extensions.Literal["spread"] | None: ...

global___S3Table = S3Table

@typing_extensions.final
class KafkaTopic(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_FIELD_NUMBER: builtins.int
    TOPIC_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    @property
    def db(self) -> global___ExtDatabase: ...
    topic: builtins.str
    @property
    def format(self) -> global___KafkaFormat: ...
    def __init__(
        self,
        *,
        db: global___ExtDatabase | None = ...,
        topic: builtins.str = ...,
        format: global___KafkaFormat | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["db", b"db", "format", b"format"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["db", b"db", "format", b"format", "topic", b"topic"]) -> None: ...

global___KafkaTopic = KafkaTopic

@typing_extensions.final
class BigqueryTable(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    @property
    def db(self) -> global___ExtDatabase: ...
    table_name: builtins.str
    def __init__(
        self,
        *,
        db: global___ExtDatabase | None = ...,
        table_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["db", b"db"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["db", b"db", "table_name", b"table_name"]) -> None: ...

global___BigqueryTable = BigqueryTable

@typing_extensions.final
class SnowflakeTable(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    @property
    def db(self) -> global___ExtDatabase: ...
    table_name: builtins.str
    def __init__(
        self,
        *,
        db: global___ExtDatabase | None = ...,
        table_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["db", b"db"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["db", b"db", "table_name", b"table_name"]) -> None: ...

global___SnowflakeTable = SnowflakeTable

@typing_extensions.final
class WebhookEndpoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    @property
    def db(self) -> global___ExtDatabase: ...
    endpoint: builtins.str
    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        db: global___ExtDatabase | None = ...,
        endpoint: builtins.str = ...,
        duration: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["db", b"db", "duration", b"duration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["db", b"db", "duration", b"duration", "endpoint", b"endpoint"]) -> None: ...

global___WebhookEndpoint = WebhookEndpoint

@typing_extensions.final
class KinesisStream(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_ARN_FIELD_NUMBER: builtins.int
    INIT_POSITION_FIELD_NUMBER: builtins.int
    INIT_TIMESTAMP_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    DB_FIELD_NUMBER: builtins.int
    stream_arn: builtins.str
    init_position: kinesis_pb2.InitPosition.ValueType
    @property
    def init_timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    format: builtins.str
    @property
    def db(self) -> global___ExtDatabase: ...
    def __init__(
        self,
        *,
        stream_arn: builtins.str = ...,
        init_position: kinesis_pb2.InitPosition.ValueType = ...,
        init_timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        format: builtins.str = ...,
        db: global___ExtDatabase | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["db", b"db", "init_timestamp", b"init_timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["db", b"db", "format", b"format", "init_position", b"init_position", "init_timestamp", b"init_timestamp", "stream_arn", b"stream_arn"]) -> None: ...

global___KinesisStream = KinesisStream

@typing_extensions.final
class RedshiftTable(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_FIELD_NUMBER: builtins.int
    SCHEMA_NAME_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    @property
    def db(self) -> global___ExtDatabase: ...
    schema_name: builtins.str
    table_name: builtins.str
    def __init__(
        self,
        *,
        db: global___ExtDatabase | None = ...,
        schema_name: builtins.str = ...,
        table_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["db", b"db"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["db", b"db", "schema_name", b"schema_name", "table_name", b"table_name"]) -> None: ...

global___RedshiftTable = RedshiftTable

@typing_extensions.final
class PreProcValue(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REF_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    ref: builtins.str
    @property
    def value(self) -> schema_pb2.Value: ...
    def __init__(
        self,
        *,
        ref: builtins.str = ...,
        value: schema_pb2.Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ref", b"ref", "value", b"value", "variant", b"variant"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ref", b"ref", "value", b"value", "variant", b"variant"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["variant", b"variant"]) -> typing_extensions.Literal["ref", "value"] | None: ...

global___PreProcValue = PreProcValue

@typing_extensions.final
class MongoCollection(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_FIELD_NUMBER: builtins.int
    COLLECTION_NAME_FIELD_NUMBER: builtins.int
    @property
    def db(self) -> global___ExtDatabase: ...
    collection_name: builtins.str
    def __init__(
        self,
        *,
        db: global___ExtDatabase | None = ...,
        collection_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["db", b"db"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["collection_name", b"collection_name", "db", b"db"]) -> None: ...

global___MongoCollection = MongoCollection

@typing_extensions.final
class Source(google.protobuf.message.Message):
    """-----------------------------------------
    Finally, all the sources and sinks
    -----------------------------------------
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class PreProcEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___PreProcValue: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___PreProcValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    TABLE_FIELD_NUMBER: builtins.int
    DATASET_FIELD_NUMBER: builtins.int
    DS_VERSION_FIELD_NUMBER: builtins.int
    EVERY_FIELD_NUMBER: builtins.int
    CURSOR_FIELD_NUMBER: builtins.int
    DISORDER_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_FIELD_NUMBER: builtins.int
    CDC_FIELD_NUMBER: builtins.int
    STARTING_FROM_FIELD_NUMBER: builtins.int
    PRE_PROC_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    BOUNDED_FIELD_NUMBER: builtins.int
    IDLENESS_FIELD_NUMBER: builtins.int
    UNTIL_FIELD_NUMBER: builtins.int
    @property
    def table(self) -> global___ExtTable: ...
    dataset: builtins.str
    ds_version: builtins.int
    @property
    def every(self) -> google.protobuf.duration_pb2.Duration: ...
    cursor: builtins.str
    @property
    def disorder(self) -> google.protobuf.duration_pb2.Duration: ...
    timestamp_field: builtins.str
    cdc: global___CDCStrategy.ValueType
    @property
    def starting_from(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def pre_proc(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___PreProcValue]: ...
    version: builtins.int
    bounded: builtins.bool
    @property
    def idleness(self) -> google.protobuf.duration_pb2.Duration: ...
    @property
    def until(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        table: global___ExtTable | None = ...,
        dataset: builtins.str = ...,
        ds_version: builtins.int = ...,
        every: google.protobuf.duration_pb2.Duration | None = ...,
        cursor: builtins.str | None = ...,
        disorder: google.protobuf.duration_pb2.Duration | None = ...,
        timestamp_field: builtins.str = ...,
        cdc: global___CDCStrategy.ValueType = ...,
        starting_from: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        pre_proc: collections.abc.Mapping[builtins.str, global___PreProcValue] | None = ...,
        version: builtins.int = ...,
        bounded: builtins.bool = ...,
        idleness: google.protobuf.duration_pb2.Duration | None = ...,
        until: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_cursor", b"_cursor", "_idleness", b"_idleness", "cursor", b"cursor", "disorder", b"disorder", "every", b"every", "idleness", b"idleness", "starting_from", b"starting_from", "table", b"table", "until", b"until"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_cursor", b"_cursor", "_idleness", b"_idleness", "bounded", b"bounded", "cdc", b"cdc", "cursor", b"cursor", "dataset", b"dataset", "disorder", b"disorder", "ds_version", b"ds_version", "every", b"every", "idleness", b"idleness", "pre_proc", b"pre_proc", "starting_from", b"starting_from", "table", b"table", "timestamp_field", b"timestamp_field", "until", b"until", "version", b"version"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_cursor", b"_cursor"]) -> typing_extensions.Literal["cursor"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_idleness", b"_idleness"]) -> typing_extensions.Literal["idleness"] | None: ...

global___Source = Source

@typing_extensions.final
class Sink(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TABLE_FIELD_NUMBER: builtins.int
    DATASET_FIELD_NUMBER: builtins.int
    @property
    def table(self) -> global___ExtTable: ...
    dataset: builtins.str
    def __init__(
        self,
        *,
        table: global___ExtTable | None = ...,
        dataset: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["table", b"table"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset", b"dataset", "table", b"table"]) -> None: ...

global___Sink = Sink
