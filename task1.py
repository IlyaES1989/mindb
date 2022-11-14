import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from copy import deepcopy


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
        1,
    )
    frame["session_id"] = (
        frame.loc[frame["session_id"] == 1].groupby("session_id").cumcount()
    )
    frame["session_id"] = frame["session_id"].ffill().astype(int)
    return frame


if __name__ == "__main__":
    AMOUNT = 10**7
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=10)

    df = pd.DataFrame(
        {
            "customer_id": np.random.randint(0, AMOUNT, AMOUNT),
            "product_id": np.random.randint(100, 2 * AMOUNT, AMOUNT),
            "timestamp": np.array(
                np.random.randint(start_time.timestamp(), end_time.timestamp(), AMOUNT),
                dtype="datetime64[s]",
            ),
        }
    )

    df = set_session_id(df)
    print(df)

