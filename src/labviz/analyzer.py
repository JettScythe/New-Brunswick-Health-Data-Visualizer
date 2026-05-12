from pandas import DataFrame


def summarize(df: DataFrame):
    return df.groupby(["obs_code", "obs_name"])["value"].describe()


def group_series(df: DataFrame):
    return df.groupby(["obs_code", "obs_name"])
