# generate_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_stock_data(file_path, start_date="2023-01-01", days=150):
    dates = pd.date_range(start=start_date, periods=days)
    # Create synthetic stock prices: start at 100 and add random noise cumulatively.
    prices = 100 + np.cumsum(np.random.randn(days))
    df = pd.DataFrame({'Date': dates, 'Price': prices})
    df.to_csv(file_path, index=False)
    print(f"Sample data generated and saved to {file_path}")

if __name__ == '__main__':
    generate_stock_data("stock_data.csv")
