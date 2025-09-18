# src/data_processing.py

import pandas as pd

def load_and_prepare_data(file_path: str) -> pd.DataFrame:
    """
    Loads the raw yield data from a CSV file.
    Ensures the 'DATE' column is parsed as datetime and set as the index.
    """
    print("⚙️ Loading and preparing data for visualization...")
    
    df = pd.read_csv(file_path, index_col="DATE", parse_dates=True)
    
    # Check for missing values which might need handling
    if df.isnull().values.any():
        print("⚠️ Warning: Missing values detected in the data.")
        # Optional: df = df.ffill() # Forward fill missing values
        
    print("✅ Data is ready.")
    return df