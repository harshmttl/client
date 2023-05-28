from datetime import datetime

import pandas as pd
import pytest

from fennel.datasets import dataset, field
from fennel.datasets import pipeline, Dataset
from fennel.featuresets import featureset, extractor, feature
from fennel.lib.aggregate import Count
from fennel.lib.expectations import (
    expectations,
    expect_column_values_to_be_between,
)
from fennel.lib.metadata import meta
from fennel.lib.schema import inputs, outputs
from fennel.lib.window import Window
from fennel.sources import S3, Webhook
from fennel.sources import source
from fennel.test_lib import mock

s3 = S3(
    name="outbrain_source",
    aws_access_key_id="AKIA3EK5WO5OPRXWZE5V",
    aws_secret_access_key="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",
)

webhook = Webhook(name="outbrain_webhook")

MIN_TIMESTAMP = 1683220303091


@source(
    s3.bucket(
        "fennel-demo-data",
        prefix="outbrain/page_views_filter.csv",
    ),
    every="1d",
)
@meta(owner="xiao@fennel.ai")
@dataset
class PageViews:
    uuid: str
    document_id: int
    timestamp: datetime
    platform: int
    geo_location: str
    traffic_source: int


@meta(owner="xiao@fennel.ai")
@dataset
class PageViewsByUser:
    uuid: str = field(key=True)
    page_views: int
    page_views_1d: int
    page_views_3d: int
    page_views_9d: int
    timestamp: datetime = field(timestamp=True)

    @pipeline(version=1)
    @inputs(PageViews)
    def group_by_user(cls, page_views: Dataset):
        return page_views.groupby("uuid").aggregate(
            [
                Count(window=Window("28d"), into_field="page_views"),
                Count(window=Window("1d"), into_field="page_views_1d"),
                Count(window=Window("3d"), into_field="page_views_3d"),
                Count(window=Window("9d"), into_field="page_views_9d"),
            ]
        )

    @expectations
    def get_expectations(cls):
        return [
            expect_column_values_to_be_between(
                column="page_views", min_value=1, max_value=100, mostly=0.95
            )
        ]


@meta(owner="aditya@fennel.ai")
@featureset
class Request:
    uuid: str = feature(id=1)
    document_id: int = feature(id=2)


@meta(owner="aditya@fennel.ai")
@featureset
class UserPageViewFeatures:
    page_views: int = feature(id=1)
    page_views_1d: int = feature(id=2)
    page_views_3d: int = feature(id=3)
    page_views_9d: int = feature(id=4)

    @extractor(depends_on=[PageViewsByUser], version=2)
    @inputs(Request.uuid)
    @outputs(page_views, page_views_1d, page_views_3d, page_views_9d)
    def extract(cls, ts: pd.Series, uuids: pd.Series):
        page_views, found = PageViewsByUser.lookup(  # type: ignore
            ts, uuid=uuids
        )
        ret = page_views[
            ["page_views", "page_views_1d", "page_views_3d", "page_views_9d"]
        ]
        ret = ret.fillna(0)
        ret["page_views"] = ret["page_views"].astype(int)
        ret["page_views_1d"] = ret["page_views_1d"].astype(int)
        ret["page_views_3d"] = ret["page_views_3d"].astype(int)
        ret["page_views_9d"] = ret["page_views_9d"].astype(int)
        return ret


@pytest.mark.slow
@pytest.mark.integration
@mock
def test_outbrain(client):
    fake_PageViews = PageViews.with_source(webhook.endpoint("PageViews"))
    client.sync(
        datasets=[
            fake_PageViews,
            PageViewsByUser,
        ],
        featuresets=[
            Request,
            UserPageViewFeatures,
        ],
    )
    df = pd.read_csv("fennel/client_tests/data/page_views_sample.csv")
    # Current time 10 days from today in ms
    cur_time_ms = datetime.now().timestamp() * 1000
    ten_days_ago = cur_time_ms - 10 * 24 * 60 * 60 * 1000
    df["timestamp"] = df["timestamp"] - MIN_TIMESTAMP + ten_days_ago
    # Add a current row timestamp in the dataframe

    # Current time in ms
    new_row = {
        "uuid": "100016de3e1e8c1",
        "document_id": 20330891,
        "timestamp": cur_time_ms,
        "platform": 2,
        "geo_location": "US>CA>808",
        "traffic_source": 1,
    }

    # create a DataFrame with the new row data
    df_new = pd.DataFrame([new_row])
    df = pd.concat([df, df_new], ignore_index=True)

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

    client.log("outbrain_webhook", "PageViews", df)
    if client.is_integration_client():
        client.sleep(120)

    df = df.iloc[:-1, :]
    input_df = df.copy()
    input_df = input_df[["uuid", "document_id"]]
    input_df.rename(
        columns={
            "uuid": "Request.uuid",
            "document_id": "Request.document_id",
        },
        inplace=True,
    )
    input_df = input_df.reset_index(drop=True)
    feature_df = client.extract_features(
        output_feature_list=[
            Request,
            UserPageViewFeatures,
        ],
        input_feature_list=[Request],
        input_dataframe=input_df,
    )
    assert feature_df.shape[0] == 399
    assert feature_df["UserPageViewFeatures.page_views"].sum() == 12971
    assert feature_df["UserPageViewFeatures.page_views_1d"].sum() == 943
    assert feature_df["UserPageViewFeatures.page_views_3d"].sum() == 4065
    assert feature_df["UserPageViewFeatures.page_views_9d"].sum() == 10083