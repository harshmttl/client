from datetime import datetime

import pandas as pd
from typing import Optional

from fennel.datasets import dataset, field, Dataset, pipeline
from fennel.featuresets import featureset, feature, extractor
from fennel.lib.aggregate import Sum
from fennel.lib.includes import includes
from fennel.lib.metadata import meta
from fennel.lib.schema import inputs, outputs
from fennel.lib.to_proto.source_code import (
    get_featureset_core_code,
    get_dataset_core_code,
    lambda_to_python_regular_func,
)
from fennel.lib.window import Window


@meta(owner="me@fennel.ai")
@dataset
class UserAge:
    name: str = field(key=True)
    age: int
    city: str
    timestamp: datetime


@meta(owner="me@fennel.ai")
@dataset
class UserAgeNonTable:
    name: str
    age: int
    city: str
    timestamp: datetime


@dataset
class UserAgeAggregated:
    city: str = field(key=True)
    timestamp: datetime
    sum_age: int

    @pipeline(id=1)
    @inputs(UserAge)
    def create_user_age_aggregated(cls, user_age: Dataset):
        return user_age.groupby("city").aggregate(
            [
                Sum(
                    window=Window("1w"),
                    of="age",
                    into_field="sum_age",
                )
            ]
        )

    @pipeline(id=2)
    @inputs(UserAgeNonTable)
    def create_user_age_aggregated2(cls, user_age: Dataset):
        return user_age.groupby("city").aggregate(
            [
                Sum(
                    window=Window("1w"),
                    of="age",
                    into_field="sum_age",
                )
            ]
        )


@dataset
class User:
    uid: int = field(key=True)
    dob: datetime
    country: str
    signup_time: datetime = field(timestamp=True)


@featureset
class UserFeature:
    uid: int = feature(id=1)
    country: str = feature(id=2)
    age: float = feature(id=3)
    dob: datetime = feature(id=4)

    @extractor
    @inputs(uid)
    @outputs(age)
    def get_age(cls, ts: pd.Series, uids: pd.Series):
        dobs = User.lookup(ts=ts, uid=uids, fields=["dob"])  # type: ignore
        ages = [dob - datetime.now() for dob in dobs]
        return pd.Series(ages)

    @extractor(depends_on=[User])
    @inputs(uid)
    @outputs(country)
    def get_country(cls, ts: pd.Series, uids: pd.Series):
        countries, _ = User.lookup(  # type: ignore
            ts=ts, uid=uids, fields=["country"]
        )
        return countries


@meta(owner="test@test.com")
@dataset
class UserInfoDataset:
    user_id: int = field(key=True)
    name: str
    age: Optional[int]
    timestamp: datetime = field(timestamp=True)
    country: str


def square(x: int) -> int:
    return x**2


def cube(x: int) -> int:
    return x**3


@includes(square)
def power_4(x: int) -> int:
    return square(square(x))


@featureset
class UserInfoExtractor:
    userid: int = feature(id=1)
    age: int = feature(id=4)
    age_power_four: int = feature(id=5)
    age_cubed: int = feature(id=6)
    is_name_common: bool = feature(id=7)

    @extractor(depends_on=[UserInfoDataset])
    @includes(power_4, cube)
    @inputs(userid)
    @outputs(age, age_power_four, age_cubed, is_name_common)
    def get_user_info(cls, ts: pd.Series, user_id: pd.Series):
        df, _ = UserInfoDataset.lookup(ts, user_id=user_id)  # type: ignore
        df[str(cls.userid)] = user_id
        df[str(cls.age_power_four)] = power_4(df["age"])
        df[str(cls.age_cubed)] = cube(df["age"])
        df[str(cls.is_name_common)] = df["name"].isin(["John", "Mary", "Bob"])
        return df[
            [
                str(cls.age),
                str(cls.age_power_four),
                str(cls.age_cubed),
                str(cls.is_name_common),
            ]
        ]


def test_source_code_gen():
    expected_source_code = """
@featureset
class UserFeature:
    uid: int = feature(id=1)
    country: str = feature(id=2)
    age: float = feature(id=3)
    dob: datetime = feature(id=4)
"""

    assert expected_source_code == get_featureset_core_code(UserFeature)
    expected_source_code = """
@dataset
class UserAgeAggregated:
    city: str = field(key=True)
    timestamp: datetime
    sum_age: int
"""
    assert expected_source_code == get_dataset_core_code(UserAgeAggregated)

    expected_source_code = """
@featureset
class UserInfoExtractor:
    userid: int = feature(id=1)
    age: int = feature(id=4)
    age_power_four: int = feature(id=5)
    age_cubed: int = feature(id=6)
    is_name_common: bool = feature(id=7)
"""
    assert expected_source_code == get_featureset_core_code(UserInfoExtractor)


def test_lambda_source_code_gen():
    a1 = "lambda x: x + 1"
    expected_source_code = """
def lambda_func(x):
    return x + 1
"""
    assert expected_source_code == lambda_to_python_regular_func(a1)
    a2 = """lambda df: df["club"] == "Manchester United" """
    expected_source_code = """
def lambda_func(df):
    return df["club"] == "Manchester United"
"""

    assert expected_source_code == lambda_to_python_regular_func(a2)

    a3 = """lambda df: df["club"] == "Manchester United" and df["age"] > 20"""
    expected_source_code = """
def lambda_func(df):
    return df["club"] == "Manchester United" and df["age"] > 20
"""
    assert expected_source_code == lambda_to_python_regular_func(a3)

    a4 = """lambda df: df["club"] == "Manchester United" and df["age"] > 20 and df["name"] == "Ronaldo" """
    expected_source_code = """
def lambda_func(df):
    return df["club"] == "Manchester United" and df["age"] > 20 and df["name"] == "Ronaldo"
"""
    assert expected_source_code == lambda_to_python_regular_func(a4)

    a5 = """filtered_ds = activity.filter(lambda df: df["action_type"] == "report")"""
    expected_source_code = """
def lambda_func(df):
    return df["action_type"] == "report"
"""
    assert expected_source_code == lambda_to_python_regular_func(a5)

    a6 = """filtered_ds = rating.filter(lambda df: df["rating"] >= 3.5)"""
    expected_source_code = """
def lambda_func(df):
    return df["rating"] >= 3.5
"""
    assert expected_source_code == lambda_to_python_regular_func(a6)

    a7 = """lambda df: df["club"] == "Manchester United")"""
    expected_source_code = """
def lambda_func(df):
    return df["club"] == "Manchester United"
"""
    assert expected_source_code == lambda_to_python_regular_func(a7)

    a8 = """lambda df: df["club"] == "Manchester United"))"""
    assert expected_source_code == lambda_to_python_regular_func(a8)

    a9 = """(lambda df: df["club"] == "Manchester United")"""
    assert expected_source_code == lambda_to_python_regular_func(a9)

    a10 = """lambda df: df.fillna({"city": "unknown"}),"""
    expected_source_code = """
def lambda_func(df):
    return df.fillna({"city": "unknown"})
"""
    assert expected_source_code == lambda_to_python_regular_func(a10)