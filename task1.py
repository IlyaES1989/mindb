import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from copy import deepcopy


def timestamp_generation() -> pd.Timestamp:
    delta = random.randint(0, 60)
    return pd.Timestamp(datetime.now() + timedelta(minutes=delta))


class SessionId:
    _session_id = 0
    _customer_id = None
    _timestamp = None

    @classmethod
    def next_session_id(cls, *args):
        cls._session_id += 1
        return cls._session_id


def set_session_id(frame: pd.DataFrame) -> pd.DataFrame:
    frame = deepcopy(frame)
    frame.sort_values(
        [
            "customer_id",
            "timestamp",
        ],
        ignore_index=True,
        inplace=True,
    )

    frame["session_id"] = np.where(
        (
            (frame.customer_id == frame.customer_id.shift())
            & (frame.timestamp - frame.timestamp.shift() < pd.Timedelta("00:03:00"))
        ),
        np.nan,
        frame.apply(SessionId.next_session_id, axis=1),
    )
    frame["session_id"] = frame["session_id"].ffill().astype(int)
    return frame


if __name__ == "__main__":
    AMOUNT = 10**2

    df = pd.DataFrame(
        {
            "customer_id": [random.randint(0, 20) for _ in range(AMOUNT)],
            "product_id": [random.randint(200, 100_000) for _ in range(AMOUNT)],
            "timestamp": [timestamp_generation() for i in range(AMOUNT)],
        }
    )
    start = datetime.now()

    df = set_session_id(df)
    print(df)

