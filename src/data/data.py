import pandas as pd


def load_data(datadir: str) -> pd.DataFrame:
    return pd.concat(
        [
            pd.read_csv(f"{datadir}/X.csv", index_col=0),
            pd.read_csv(f"{datadir}/y.csv", index_col=0)
        ],
        axis=1)
