from datetime import datetime

from fennel import sources
from fennel.datasets import dataset, field
from fennel.lib.metadata import meta
from fennel.sources import source

# docsnip mysql_source
mysql = sources.MySQL(
    name="py_mysql_src",
    host="my-favourite-mysql.us-west-2.rds.amazonaws.com",
    port=3306,
    db_name="some_database_name",
    username="admin",
    password="password",
    jdbc_params="enabledTLSProtocols=TLSv1.2",
)


@source(mysql.table("user", cursor="update_time"), every="1m")
@dataset
class UserMysqlSourcedDataset:
    uid: int = field(key=True)
    email: str
    timestamp: datetime
    ...


# /docsnip


# docsnip postgres_source
postgres = sources.Postgres(
    name="py_psql_src",
    host="my-favourite-postgres.us-west-2.rds.amazonaws.com",
    db_name="some_database_name",
    username="admin",
    password="password",
)


@source(postgres.table("user", cursor="update_time"), every="1m")
@dataset
class UserPostgresSourcedDataset:
    uid: int
    timestamp: datetime
    ...


# /docsnip

# docsnip s3_source
s3 = sources.S3(
    name="ratings_source",
    aws_access_key_id="<SOME_ACCESS_KEY>",
    aws_secret_access_key="<SOME_SECRET_ACCESS_KEY>",
)


@source(s3.bucket("engagement", prefix="notion"), every="30m")
@meta(owner="abc@email.com")
@dataset
class UserS3SourcedDataset:
    uid: int = field(key=True)
    email: str
    timestamp: datetime
    ...


# /docsnip

# docsnip snowflake_source
sf_src = sources.Snowflake(
    name="snowflake_src",
    account="nhb38793.us-west-2.snowflakecomputing.com",
    warehouse="TEST",
    schema="PUBLIC",
    db_name="TEST_DB",
    src_schema="PUBLIC",
    role="ACCOUNTADMIN",
    username="<username>",
    password="<password>",
)
# /docsnip