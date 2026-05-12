from json import dump


def to_csv(df, path="lab_results.csv"):
    df.to_csv(path, index=False)


def to_ai_json(df, path="lab_results_ai.json"):
    output = {}

    for (code, name), group in df.groupby(["obs_code", "obs_name"]):
        output[name] = [
            {"date": str(row.date), "value": row.value, "unit": row.unit}
            for row in group.itertuples()
        ]

    with open(path, "w") as f:
        dump(output, f, indent=2)
