from datetime import datetime
from typing import Optional, Tuple

import pandas as pd
import pytest

from fennel.datasets import dataset, field
from fennel.featuresets import featureset, extractor, depends_on, feature

# noinspection PyUnresolvedReferences
from fennel.test_lib import *


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


@featureset
class User:
    id: int = feature(id=1)
    age: float = feature(id=2)


def test_ComplexFeatureSet(grpc_stub):
    with pytest.raises(TypeError) as e:

        @featureset
        class UserInfo:
            userid: int = feature(id=1)
            home_geoid: int = feature(id=2)
            # The users gender among male/female/non-binary
            gender: str = feature(id=3)
            age: int = feature(id=4).meta(owner="aditya@fennel.ai")
            income: int = feature(id=5)

            @extractor
            @depends_on(UserInfoDataset)
            def get_user_info1(
                ts: pd.Series, user_id: User.id
            ) -> Tuple["userid", "home_geoid"]:
                pass

            @extractor
            @depends_on(UserInfoDataset)
            def get_user_info2(
                ts: pd.Series, user_id: User.id
            ) -> Tuple["gender", "age"]:
                pass

            @extractor
            def get_user_info3(
                ts: pd.Series, user_id: User.id
            ) -> Tuple["gender"]:
                pass

    assert str(e.value) == "Feature gender is extracted by multiple extractors"


def test_MissingId(grpc_stub):
    with pytest.raises(TypeError) as e:

        @featureset
        class UserInfo:
            userid: int = feature()
            home_geoid: int = feature(id=2)

    assert (
        str(e.value) == "feature() missing 1 required positional argument: 'id'"
    )


def test_DuplicateId(grpc_stub):
    with pytest.raises(ValueError) as e:

        @featureset
        class UserInfo:
            userid: int = feature(id=1)
            home_geoid: int = feature(id=2)
            age: int = feature(id=1)

    assert str(e.value) == "Feature age has a duplicate id 1"


def test_DeprecatedId(grpc_stub):
    with pytest.raises(ValueError) as e:

        @featureset
        class UserInfo:
            userid: int = feature(id=1)
            home_geoid: int = feature(id=2)
            age: int = feature(id=3).meta(deprecated=True)
            credit_score: int = feature(id=3)

    assert str(e.value) == "Feature credit_score has a duplicate id 3"