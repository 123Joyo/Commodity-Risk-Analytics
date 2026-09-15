from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import AutoMinorLocator, MaxNLocator

from src.returns import*

def plot_all_charts(df: pd.DataFrame, ) -> pd.DataFrame | None:

    
    pass

def plot_historical_prices(
    plot_name: str,
    df: pd.DataFrame,
    columns: str | list[str],
    output_path: str | Path,
    subplots: bool = False,
    date_frequency: str = "yearly",
) -> None:
    if isinstance(columns, str):
        columns = [columns]

    plot_df = df.sort_values("date")

    axes = plot_df.plot(
        x="date",
        y=columns,
        subplots=subplots,
        figsize=(13, 4 * len(columns) if subplots else 7),
        sharex=True,
        linewidth=1.2,
        alpha=0.9,
        grid=False,
    )

    # Make axes iterable whether there is one plot or several.
    axes = [axes] if not subplots else list(axes)

    date_locators = {
        "yearly": (
            mdates.YearLocator(),
            mdates.DateFormatter("%Y"),
        ),
        "monthly": (
            mdates.MonthLocator(),
            mdates.DateFormatter("%b %Y"),
        ),
        "weekly": (
            mdates.WeekdayLocator(byweekday=mdates.MO),
            mdates.DateFormatter("%d %b %Y"),
        ),
        "daily": (
            mdates.DayLocator(),
            mdates.DateFormatter("%d %b %Y"),
        ),
    }

    if date_frequency not in date_locators:
        raise ValueError(
            "date_frequency must be 'yearly', 'monthly', "
            "'weekly', or 'daily'."
        )

    date_locator, date_formatter = date_locators[date_frequency]

    for ax in axes:
        ax.set_ylabel("Price")
        ax.set_xlabel("")

        # More readable date ticks.
        ax.xaxis.set_major_locator(date_locator)
        ax.xaxis.set_major_formatter(date_formatter)

        ax.tick_params(
            axis="x",
            labelrotation=45 if date_frequency != "yearly" else 0,
        )

        # More horizontal price lines.
        ax.yaxis.set_major_locator(MaxNLocator(nbins=10))
        ax.yaxis.set_minor_locator(AutoMinorLocator(2))

        ax.grid(
            which="major",
            axis="both",
            linestyle="--",
            linewidth=0.6,
            alpha=0.5,
        )
        ax.grid(
            which="minor",
            axis="y",
            linestyle=":",
            linewidth=0.4,
            alpha=0.3,
        )

        # Only show zero when it is relevant to the plotted range.
        lower, upper = ax.get_ylim()

        if lower <= 0 <= upper:
            ax.axhline(
                0,
                color="black",
                linewidth=0.9,
                alpha=0.7,
            )

        ax.margins(x=0.01)

        # Add or improve the legend.
        ax.legend(
            loc="best",
            frameon=False,
            ncols=min(len(columns), 4),
        )

        # Remove unnecessary borders.
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    axes[-1].set_xlabel("Date")

    plt.suptitle(
        plot_name,
        fontsize=15,
        fontweight="semibold",
    )
    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=200,
        bbox_inches="tight",
    )
    plt.show()
    plt.close()