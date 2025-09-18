# main.py

from src.data_ingestion import fetch_and_save_yields
from src.data_processing import load_and_prepare_data
from src.visualization import plot_yield_and_spread
from src import config

def main():
    """
    Main function to run the entire data pipeline.
    """
    # Step 1: Fetch data from the source and save it.
    fetch_and_save_yields()

    # Step 2: Load and prepare the data for analysis.
    processed_df = load_and_prepare_data(config.RAW_DATA_PATH)

    # Step 3: Generate and save visualizations.
    if not processed_df.empty:
        plot_yield_and_spread(processed_df)
    else:
        print("❌ No data to visualize. Skipping visualization step.")

    print("\n🎉 Pipeline finished successfully!")

if __name__ == '__main__':
    main()