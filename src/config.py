# src/config.py

import datetime

# =======================
# Paths
# =======================
RAW_DATA_PATH = "data/raw/us_treasury_yields_Mar2025.csv"
FIGURES_PATH = "reports/figures/"

# =======================
# Data Ingestion Parameters
# =======================
START_DATE = datetime.datetime(2025, 3, 1)
END_DATE = datetime.datetime(2025, 3, 31)
YIELD_TICKERS_MAP = {
    "DGS2": "DGS2",   # 2 Year Treasury
    "DGS10": "DGS10"  # 10 Year Treasury
}
