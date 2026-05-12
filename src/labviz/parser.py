from json import load
from pandas import DataFrame, to_datetime


def load_json(path: str):
    with open(path, "r") as f:
        data = load(f)
        return data["data"]


def flatten_reports(data: list[dict]):
    rows = []

    for report in data:
        report_date = report.get("effectiveDate")

        observations = report.get("observations", [])
        if not observations:
            continue

        for obs in observations:
            # raw fields
            value = obs.get("resultValueQuantity")
            code = obs.get("observationCode")
            name = obs.get("observationCodeDisplay")

            # skip missing essentials
            if value is None or code is None:
                continue

            # convert value safely
            try:
                value = float(value)
            except TypeError, ValueError:
                continue

            rows.append(
                {
                    "obs_code": str(code),
                    "obs_name": str(name) if name is not None else str(code),
                    "date": report_date,
                    "value": value,
                    "unit": obs.get("resultValueUnits"),
                    "ref_range": obs.get("referenceRange"),
                    "interpretation": obs.get("interpretationCode"),
                }
            )
    df = DataFrame(rows)
    df["date"] = to_datetime(df["date"], errors="coerce")

    df = df.dropna(subset=["obs_code", "date", "value"])
    df = df.sort_values("date")

    return df
