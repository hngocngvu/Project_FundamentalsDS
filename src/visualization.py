# src/visualization.py

import matplotlib.pyplot as plt
import os
from src import config

def save_plot(fig, filename: str):
    """Saves a matplotlib figure to the reports/figures directory."""
    os.makedirs(config.FIGURES_PATH, exist_ok=True)
    path = os.path.join(config.FIGURES_PATH, filename)
    fig.savefig(path, dpi=200, bbox_inches='tight')
    print(f"📈 Plot saved to {path}")
    plt.close(fig)

def plot_yield_and_spread(df: pd.DataFrame):
    """
    Plots the 2Y, 10Y yields and their spread over time.
    """
    print("🎨 Generating yield and spread plot...")
    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot the yields
    df[['DGS2', 'DGS10']].plot(ax=ax, marker='.', linestyle='-')
    
    # Plot the spread on the same axis
    df['Spread_10Y_2Y'].plot(ax=ax, color='purple', linestyle='--', label='Spread (10Y-2Y)')

    # Formatting
    ax.set_title(f'US Treasury Yields & Spread ({df.index.min().date()} to {df.index.max().date()})')
    ax.set_ylabel('Yield (%)')
    ax.set_xlabel('Date')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    
    # Add a horizontal line at zero for spread context
    ax.axhline(0, color='red', linestyle=':', linewidth=1.2, label='Inversion Threshold')

    save_plot(fig, 'yield_spread_Mar2025.png')