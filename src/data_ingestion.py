# src/data_ingestion.py

import pandas as pd
import pandas_datareader.data as web
from src import config
import os

def fetch_and_save_yields():
    """
    Fetches 2Y and 10Y treasury yields from FRED for a specific period,
    calculates the spread, and saves the result to a CSV file.
    """
    print(f"🚀 Fetching data from {config.START_DATE.date()} to {config.END_DATE.date()}...")

    # Fetch data for each ticker
    dgs2 = web.DataReader("DGS2", "fred", config.START_DATE, config.END_DATE)
    dgs10 = web.DataReader("DGS10", "fred", config.START_DATE, config.END_DATE)

    # Join the series into a single DataFrame
    yields = dgs2.join(dgs10, how="outer")
    yields.columns = ["DGS2", "DGS10"]

    # Calculate the yield spread
    yields["Spread_10Y_2Y"] = yields["DGS10"] - yields["DGS2"]
    
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(config.RAW_DATA_PATH), exist_ok=True)

    # Save to the raw data path defined in config
    yields.to_csv(config.RAW_DATA_PATH)
    
    print(f"✅ Data successfully saved to {config.RAW_DATA_PATH}")
    print("Data head:")
    print(yields.head())