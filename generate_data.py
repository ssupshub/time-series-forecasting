# generate_data.py
import pandas as pd
import numpy as np
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_stock_data(file_path, start_date="2023-01-01", days=150):
    """
    Generate synthetic stock price data and save to CSV.
    
    :param file_path: Destination CSV file path.
    :param start_date: Start date for data generation.
    :param days: Number of days of data to generate.
    """
    dates = pd.date_range(start=start_date, periods=days)
    # Create synthetic stock prices: start at 100 and add cumulative random noise.
    prices = 100 + np.cumsum(np.random.randn(days))
    df = pd.DataFrame({'Date': dates, 'Price': prices})
    df.to_csv(file_path, index=False)
    logging.info(f"Sample data generated and saved to {file_path}")

if __name__ == '__main__':
    generate_stock_data("stock_data.csv")
