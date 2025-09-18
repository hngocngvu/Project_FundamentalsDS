# src/config.py

import datetime
import os

# Cấu hình thời gian
START_DATE = datetime.datetime(2002, 1, 1)
END_DATE   = datetime.datetime(2025, 9, 13)


# Các biến kinh tế vĩ mô
MACRO_VARS = {
    "UNRATE": "Unemployment Rate",
    "FEDFUNDS": "Federal Funds Rate",
    "CPIAUCSL": "CPI (All Urban Consumers)"
}

# Các kỳ hạn treasury yields
TICKERS = [
    "DGS1MO", "DGS3MO", "DGS6MO",
    "DGS1", "DGS2", "DGS3",
    "DGS5", "DGS7", "DGS10",
    "DGS20", "DGS30"
]

# Gộp chung: tất cả series từ FRED
ALL_SERIES = list(MACRO_VARS.keys()) + TICKERS

# =======================
# Đường dẫn file
# =======================
DATA_DIR = "data"
RAW_DATA_PATH = os.path.join(DATA_DIR, "macro_treasury_full_2000.csv")


