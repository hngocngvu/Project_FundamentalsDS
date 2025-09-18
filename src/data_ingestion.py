# src/data_ingestion.py

import pandas as pd
import pandas_datareader.data as web
from src import config
import os


def fetch_data():
    print(f"Fetching data from {config.START_DATE.date()} to {config.END_DATE.date()}...")

    # Macroeconomic variables
    macro_dfs = []
    for code in config.MACRO_VARS.keys():
        macro_dfs.append(web.DataReader(code, "fred", config.START_DATE, config.END_DATE))

    # Treasury yields
    treasury = pd.DataFrame()
    for t in config.TICKERS:
        treasury[t] = web.DataReader(t, "fred", config.START_DATE, config.END_DATE)

    # Merge all
    df = pd.concat(macro_dfs + [treasury], axis=1)
    df.columns = list(config.MACRO_VARS.keys()) + config.TICKERS

    return df


def save_data(df, output_path=config.RAW_DATA_PATH):
    """
    Save DataFrame to CSV file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_csv(output_path, index=True)
    print(f"Data successfully saved to {output_path}")
