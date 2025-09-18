# main.py

from src.data_ingestion import fetch_data, save_data
from src.data_processing import load_and_prepare_data
from src.visualization import (
    plot_yield_and_spread,
    plot_macro_variables
)
from src import config


def main():
    """
    Main function to run the entire data pipeline.
    """
    print("Starting data pipeline...")

    # Step 1: Fetch data from FRED
    df = fetch_data()

    # Step 2: Save raw data to CSV
    save_data(df)

    # Step 3: Load and prepare the data for analysis
    processed_df = load_and_prepare_data(config.RAW_DATA_PATH)

    # Step 4: Generate and save visualizations
    if not processed_df.empty:
        # Plot yields & spread
        plot_yield_and_spread(processed_df)

        # Plot macroeconomic variables (if present)
        macro_cols = [col for col in config.MACRO_VARIABLES if col in processed_df.columns]
        if macro_cols:
            plot_macro_variables(processed_df, macro_cols)
        else:
            print("No macroeconomic variables found in the dataset.")
    else:
        print("No data to visualize. Skipping visualization step.")

    print("\n Pipeline finished successfully!")


if __name__ == '__main__':
    main()

