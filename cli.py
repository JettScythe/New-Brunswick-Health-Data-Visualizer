import argparse

from labviz.parser import load_json, flatten_reports
from labviz.analyzer import summarize, group_series
from labviz.plotter import plot_all
from labviz.export import to_csv, to_ai_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to JSON file")
    parser.add_argument("--export", choices=["csv", "ai-json", "all"])
    parser.add_argument("--plot", action="store_true")
    parser.add_argument("--summary", action="store_true")

    args = parser.parse_args()

    data = load_json(args.input)
    df = flatten_reports(data)

    grouped = group_series(df)

    if args.summary:
        print(summarize(df))

    if args.plot:
        plot_all(grouped)

    if args.export == "csv":
        to_csv(df)

    if args.export == "ai-json":
        to_ai_json(df)

    if args.export == "all":
        to_csv(df)
        to_ai_json(df)


if __name__ == "__main__":
    main()
