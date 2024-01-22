from datetime import datetime
from typing import Optional

import pytest

from fennel.datasets import dataset, field
from fennel.lib.metadata import meta
from fennel.sources import (
    source,
    MySQL,
    S3,
    Snowflake,
    Kafka,
    Kinesis,
)
from fennel.sources.kinesis import at_timestamp
from fennel.sources.sources import BigQuery

# noinspection PyUnresolvedReferences
from fennel.test_lib import *

mysql = MySQL(
    name="mysql",
    host="localhost",
    db_name="test",
    username="root",
    password="root",
)

snowflake = Snowflake(
    name="snowflake_src",
    account="nhb38793.us-west-2.snowflakecomputing.com",
    warehouse="TEST",
    db_name="MOVIELENS",
    src_schema="PUBLIC",
    role="ACCOUNTADMIN",
    username="<username>",
    password="<password>",
)

kafka = Kafka(
    name="kafka_src",
    bootstrap_servers="localhost:9092",
    topic="test_topic",
    group_id="test_group",
    security_protocol="PLAINTEXT",
    sasl_mechanism="PLAIN",
    sasl_plain_username="test",
    sasl_plain_password="test",
)

kinesis = Kinesis(
    name="kinesis_src",
    role_arn="arn:aws:iam::123456789012:role/test-role",
)


def test_simple_source():
    with pytest.raises(TypeError) as e:

        @source(mysql.table("user"), every="1h")
        @dataset
        class UserInfoDataset:
            user_id: int = field(key=True)
            name: str
            gender: str
            # Users date of birth
            dob: str
            age: int
            account_creation_date: datetime
            country: Optional[str]
            timestamp: datetime = field(timestamp=True)

    assert str(e.value).endswith(
        "table() missing 1 required positional argument: 'cursor'"
    )

    with pytest.raises(TypeError) as e:

        @source(mysql, every="1h")
        @dataset
        class UserInfoDataset2:
            user_id: int = field(key=True)
            name: str
            gender: str
            # Users date of birth
            dob: str
            age: int
            account_creation_date: datetime
            country: Optional[str]
            timestamp: datetime = field(timestamp=True)

    assert (
        str(e.value) == "mysql does not specify required fields table, cursor."
    )

    with pytest.raises(TypeError) as e:

        @source(mysql.table(cursor="xyz"), every="1h")
        @dataset
        class UserInfoDataset3:
            user_id: int = field(key=True)
            name: str
            gender: str
            # Users date of birth
            dob: str
            age: int
            account_creation_date: datetime
            country: Optional[str]
            timestamp: datetime = field(timestamp=True)

    assert str(e.value).endswith(
        "table() missing 1 required positional argument: 'table_name'"
    )


s3 = S3(
    name="ratings_source",
    aws_access_key_id="ALIAQOTFAKEACCCESSKEYIDGTAXJY6MZWLP",
    aws_secret_access_key="8YCvIs8f0+FAKESECRETKEY+7uYSDmq164v9hNjOIIi3q1uV8rv",
)


def test_invalid_s3_source():
    with pytest.raises(AttributeError) as e:

        @source(s3.table("user"), every="1h")
        @dataset
        class UserInfoDataset:
            user_id: int = field(key=True)
            name: str
            gender: str
            # Users date of birth
            dob: str
            age: int
            account_creation_date: datetime
            country: Optional[str]
            timestamp: datetime = field(timestamp=True)

        view = InternalTestClient()
        view.add(UserInfoDataset)
        sync_request = view._get_sync_request_proto()
        assert len(sync_request.dataset_info) == 1
        dataset_request = sync_request.dataset_info[0]
        assert len(dataset_request.sources) == 3

    assert str(e.value) == "'S3' object has no attribute 'table'"


def test_invalid_kinesis_source():
    with pytest.raises(ValueError) as e:

        @meta(owner="test@test.com")
        @source(
            kinesis.stream("test_stream", init_position=at_timestamp("today"))
        )
        @dataset
        class UserInfoDatasetKinesis1:
            user_id: int = field(key=True)
            name: str
            gender: str
            timestamp: datetime = field(timestamp=True)

    assert str(e.value) == "Invalid isoformat string: 'today'"

    with pytest.raises(TypeError) as e:

        @meta(owner="test@test.com")
        @source(kinesis.stream("test_stream", init_position=at_timestamp(None)))
        @dataset
        class UserInfoDatasetKinesis2:
            user_id: int = field(key=True)
            name: str
            gender: str
            timestamp: datetime = field(timestamp=True)

    assert str(e.value) == "Invalid timestamp type <class 'NoneType'>"

    with pytest.raises(AttributeError) as e:

        @meta(owner="test@test.com")
        @source(
            kinesis.stream(
                "test_stream",
                at_timestamp(datetime.now()),
                format="csv",
            )
        )
        @dataset
        class UserInfoDatasetKinesis3:
            user_id: int = field(key=True)
            name: str
            gender: str
            timestamp: datetime = field(timestamp=True)

    assert str(e.value) == "Kinesis format must be json"

    with pytest.raises(AttributeError) as e:

        @meta(owner="test@test.com")
        @source(
            kinesis.stream(
                "test_stream",
                "latest(2024-01-01T00:00:00Z)",
                format="csv",
            )
        )
        @dataset
        class UserInfoDatasetKinesis:
            user_id: int = field(key=True)
            name: str
            gender: str
            timestamp: datetime = field(timestamp=True)

    assert (
        str(e.value)
        == "Kinesis init position must be 'latest', 'trim_horizon' or at_timestamp(ts)"
    )


@mock
def test_multiple_sources(client):
    with pytest.raises(Exception) as e:

        @meta(owner="test@test.com")
        @source(kafka.topic("test_topic"))
        @source(mysql.table("users_mysql", cursor="added_on"), every="1h")
        @source(snowflake.table("users_Sf", cursor="added_on"), every="1h")
        @source(
            s3.bucket(
                bucket_name="all_ratings",
                prefix="prod/apac/",
            ),
            every="1h",
            disorder="2d",
        )
        @dataset
        class UserInfoDataset:
            user_id: int = field(key=True)
            name: str
            gender: str
            # Users date of birth
            dob: str
            age: int
            account_creation_date: datetime
            country: Optional[str]
            timestamp: datetime = field(timestamp=True)

        client.sync(datasets=[UserInfoDataset], featuresets=[])

    assert (
        str(e.value)
        == "Dataset `UserInfoDataset` has more than one source defined, found 4 sources."
    )


def test_invalid_bigquery_credential():
    with pytest.raises(ValueError) as e:
        BigQuery(
            name="bigquery",
            project_id="project",
            dataset_id="dataset",
            credentials_json="bad_json",
        )

    assert "can't deserialize json" in str(e.value)


def test_invalid_kaffa_security_protocol():
    with pytest.raises(ValueError) as e:
        Kafka(
            name="kafka",
            bootstrap_servers="localhost:9092",
            security_protocol="Wrong Protocol",
        )
    assert "security protocol must be one of" in str(e.value)


bigquery = BigQuery(
    name="bq_movie_tags",
    project_id="gold-cocoa-356105",
    dataset_id="movie_tags",
    credentials_json="{}",
)


def test_invalid_starting_from():
    with pytest.raises(Exception) as e:

        @meta(owner="test@test.com")
        @source(
            bigquery.table("users_bq", cursor="added_on"),
            every="1h",
            disorder="2h",
            since=datetime.now(),
        )
        @dataset
        class UserInfoDatasetBigQuery:
            user_id: int = field(key=True)
            name: str
            gender: str
            # Users date of birth
            dob: str
            age: int
            account_creation_date: datetime
            country: Optional[str]
            timestamp: datetime = field(timestamp=True)

        # bigquery source
        view = InternalTestClient()
        view.add(UserInfoDatasetBigQuery)
        _sync_request = view._get_sync_request_proto()  # noqa
    assert "BigQuery connector does not support starting_from parameter" in str(
        e.value
    )

    with pytest.raises(Exception) as e:

        @source(
            s3.bucket(bucket_name="bucket", prefix="prefix"),
            every="1h",
            since="2020-01-01T00:00:00Z",
        )
        @meta(owner="aditya@fennel.ai")
        @dataset
        class UserInfoDataset:
            user_id: int = field(key=True)
            name: str
            gender: str
            # Users date of birth
            dob: str
            age: int
            account_creation_date: datetime
            country: Optional[str]
            timestamp: datetime = field(timestamp=True)

    assert "'since' must be of type datetime - got <class 'str'>" == str(
        e.value
    )


def test_invalid_s3_format():
    with pytest.raises(Exception) as e:
        s3.bucket(bucket_name="bucket", prefix="prefix", format="py")
    assert "format must be either" in str(e.value)

    with pytest.raises(Exception) as e:
        s3.bucket(
            bucket_name="bucket", prefix="prefix", format="csv", delimiter="  "
        )
    assert "delimiter must be one of" in str(e.value)


def test_invalid_pre_proc():
    @source(
        s3.bucket(
            bucket_name="all_ratings",
            prefix="prod/apac/",
        ),
        every="1h",
        # column doesn't exist
        preproc={
            "age": 10,
        },
    )
    @meta(owner="test@test.com", tags=["test", "yolo"])
    @dataset
    class UserInfoDataset:
        user_id: int = field(key=True)
        timestamp: datetime = field(timestamp=True)

    with pytest.raises(ValueError):
        view = InternalTestClient()
        view.add(UserInfoDataset)
        view._get_sync_request_proto()

    @source(
        s3.bucket(
            bucket_name="all_ratings",
            prefix="prod/apac/",
        ),
        every="1h",
        # data type is wrong
        preproc={
            "timestamp": 10,
        },
    )
    @meta(owner="test@test.com", tags=["test", "yolo"])
    @dataset
    class UserInfoDataset2:
        user_id: int = field(key=True)
        timestamp: datetime = field(timestamp=True)

    with pytest.raises(ValueError):
        view = InternalTestClient()
        view.add(UserInfoDataset2)
        view._get_sync_request_proto()
