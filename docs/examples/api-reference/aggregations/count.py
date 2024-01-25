import unittest
from datetime import datetime

import pandas as pd

from fennel.datasets import dataset, field, pipeline, Dataset
from fennel.lib.schema import inputs
from fennel.lib.aggregate import Count
from fennel.sources import source, Webhook
from fennel.test_lib import mock

webhook = Webhook(name="webhook")
__owner__ = "aditya@fennel.ai"


class TestCountSnips(unittest.TestCase):
    @mock
    def test_basic(self, client):
        # docsnip basic
        @source(webhook.endpoint("Transaction"))
        @dataset
        class Transaction:
            uid: int
            vendor: str
            amount: int
            timestamp: datetime

        @dataset
        class Aggregated:
            uid: int = field(key=True)
            num_transactions: int
            unique_vendors_1w: int
            timestamp: datetime

            @pipeline(version=1)
            @inputs(Transaction)
            def pipeline(cls, ds: Dataset):
                return ds.groupby("uid").aggregate(
                    Count(window="forever", into_field="num_transactions"),
                    Count(
                        of="vendor",
                        unique=True,
                        approx=True,
                        window="1w",
                        into_field="unique_vendors_1w",
                    ),
                )

        # /docsnip
        client.sync(datasets=[Transaction, Aggregated])
        # log some rows to the transaction dataset
        client.log(
            "webhook",
            "Transaction",
            pd.DataFrame(
                [
                    {
                        "uid": 1,
                        "vendor": "A",
                        "amount": 10,
                        "timestamp": "2021-01-01T00:00:00",
                    },
                    {
                        "uid": 1,
                        "vendor": "B",
                        "amount": 20,
                        "timestamp": "2021-01-02T00:00:00",
                    },
                    {
                        "uid": 2,
                        "vendor": "A",
                        "amount": 30,
                        "timestamp": "2021-01-03T00:00:00",
                    },
                    {
                        "uid": 2,
                        "vendor": "B",
                        "amount": 40,
                        "timestamp": "2021-01-04T00:00:00",
                    },
                    {
                        "uid": 3,
                        "vendor": "A",
                        "amount": 50,
                        "timestamp": "2021-01-05T00:00:00",
                    },
                    {
                        "uid": 3,
                        "vendor": "B",
                        "amount": 60,
                        "timestamp": "2021-01-06T00:00:00",
                    },
                ]
            ),
        )

        # do lookup on the Aggregated dataset
        ts = pd.Series(
            [
                datetime(2021, 1, 6, 0, 0, 0),
                datetime(2021, 1, 6, 0, 0, 0),
                datetime(2021, 1, 6, 0, 0, 0),
            ]
        )
        df, found = Aggregated.lookup(ts, uid=pd.Series([1, 2, 3]))
        assert found.tolist() == [True, True, True]
        assert df["uid"].tolist() == [1, 2, 3]
        assert df["num_transactions"].tolist() == [2, 2, 2]
        assert df["unique_vendors_1w"].tolist() == [2, 2, 2]