from pandas import DataFrame
from matplotlib.pyplot import (
    figure,
    plot,
    title,
    xlabel,
    ylabel,
    xticks,
    tight_layout,
    show,
)


def plot_all(grouped_df: DataFrame):
    for (code, name), group in grouped_df:
        if len(group) < 2:
            continue

        figure()

        plot(group["date"], group["value"], marker="o")

        unit = group["unit"].dropna().iloc[0] if group["unit"].notna().any() else ""

        title(f"{name} ({code})")
        xlabel("Date")
        ylabel(f"Value {f'({unit})' if unit else ''}")

        xticks(rotation=45)
        tight_layout()

        show()
