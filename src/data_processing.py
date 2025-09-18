# src/data_processing.py

import pandas as pd
from src import config

def load_and_prepare_data(file_path: str = config.RAW_DATA_PATH) -> pd.DataFrame:

    print(f"Loading data from {file_path} ...")
    
    df = pd.read_csv(file_path, index_col="DATE", parse_dates=True)

    # Check for missing values
    if df.isnull().values.any():
        print("Missing values detected")
        df = df.ffill()  # Forward fill để tránh mất dữ liệu chuỗi thời gian
        print("Missing values forward-filled.")
    return df
