# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd
from src import config


def save_plot(fig, filename: str):
    """Saves a matplotlib figure to the reports/figures directory."""
    os.makedirs(config.FIGURES_PATH, exist_ok=True)
    path = os.path.join(config.FIGURES_PATH, filename)
    fig.savefig(path, dpi=200, bbox_inches="tight")
    print(f"📈 Plot saved to {path}")
    plt.close(fig)


def plot_macro_variables(df: pd.DataFrame):
    """
    Plots macroeconomic indicators (UNRATE, FEDFUNDS, CPI).
    """
    print("Generating macro variables plot...")
    fig, ax = plt.subplots(figsize=(12, 6))

    df[list(config.MACRO_VARS.keys())].plot(ax=ax)
    ax.set_title("Macroeconomic Indicators (UNRATE, FEDFUNDS, CPI)")
    ax.set_ylabel("Value")
    ax.set_xlabel("Date")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend()

    save_plot(fig, "macro_variables.png")


def plot_yield_curve(df: pd.DataFrame):
    """
    Plots multiple Treasury yields (1M to 30Y) over time.
    """
    print("Generating Treasury yield curve plot...")
    fig, ax = plt.subplots(figsize=(14, 7))

    df[config.TICKERS].plot(ax=ax)
    ax.set_title("US Treasury Yields (Multiple Maturities)")
    ax.set_ylabel("Yield (%)")
    ax.set_xlabel("Date")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(ncol=3)

    save_plot(fig, "yield_curve.png")


def plot_yield_spread(df: pd.DataFrame):
    """
    Plots the 2Y, 10Y yields and their spread over time.
    Spread will be computed if not present.
    """
    print("Generating yield spread plot...")

    # Nếu chưa có cột Spread thì tính
    if "Spread_10Y_2Y" not in df.columns:
        df["Spread_10Y_2Y"] = df["DGS10"] - df["DGS2"]

    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot the yields
    df[["DGS2", "DGS10"]].plot(ax=ax, marker=".", linestyle="-")

    # Plot the spread on the same axis
    df["Spread_10Y_2Y"].plot(ax=ax, color="purple", linestyle="--", label="Spread (10Y-2Y)")

    # Formatting
    ax.set_title(f"US Treasury Yields & Spread ({df.index.min().date()} to {df.index.max().date()})")
    ax.set_ylabel("Yield (%)")
    ax.set_xlabel("Date")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend()

    # Add a horizontal line at zero for spread context
    ax.axhline(0, color="red", linestyle=":", linewidth=1.2, label="Inversion Threshold")

    save_plot(fig, "yield_spread.png")


def plot_correlation_heatmap(df: pd.DataFrame):
    """
    Plots correlation heatmap of all numeric columns (macro + yields).
    """
    print("Generating correlation heatmap...")
    fig, ax = plt.subplots(figsize=(12, 8))

    corr = df.corr()
    sns.heatmap(corr, cmap="coolwarm", annot=False, ax=ax, cbar=True)
    ax.set_title("Correlation Heatmap")

    save_plot(fig, "correlation_heatmap.png")
