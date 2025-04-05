# main.py
import os
import argparse
import logging
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from utils import train_test_split

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load the CSV file containing stock data.
    Expects a 'Date' column and a 'Price' column.
    
    :param file_path: CSV file path.
    :return: Pandas DataFrame with Date as index.
    """
    if not os.path.exists(file_path):
        logging.error(f"Data file {file_path} not found!")
        raise FileNotFoundError(f"{file_path} not found.")
    try:
        data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise
    return data

def forecast_arima(train, order=(5, 1, 0), steps=30):
    """
    Build and forecast using an ARIMA model.
    
    :param train: Training data (a pandas Series).
    :param order: ARIMA model order (p, d, q).
    :param steps: Number of future steps to forecast.
    :return: Forecasted values as a pandas Series.
    """
    try:
        model = ARIMA(train, order=order)
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=steps)
    except Exception as e:
        logging.error(f"Error during ARIMA model fitting or forecasting: {e}")
        raise
    return forecast

def plot_forecast(train, test, forecast):
    """
    Plot training data, test data, and forecasted values.
    
    :param train: Training data DataFrame.
    :param test: Test data DataFrame.
    :param forecast: Forecasted values as a pandas Series.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(train.index, train['Price'], label='Training Data')
    plt.plot(test.index, test['Price'], label='Test Data')
    plt.plot(test.index, forecast, label='Forecast', color='red', linestyle='--')
    plt.title("Time Series Forecasting using ARIMA")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.legend()
    plt.tight_layout()
    plt.show()

def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Time Series Forecasting with ARIMA")
    parser.add_argument("--data_file", type=str, default="stock_data.csv", help="Path to the CSV data file")
    parser.add_argument("--order", type=int, nargs=3, default=[5, 1, 0], help="ARIMA model order as three integers: p d q")
    parser.add_argument("--forecast_steps", type=int, default=None, help="Number of steps to forecast (defaults to length of test set)")
    return parser.parse_args()

def main():
    args = parse_args()
    data_file = args.data_file
    arima_order = tuple(args.order)
    
    # Load the stock data CSV file
    data = load_data(data_file)
    
    # Split data into training and testing sets
    train, test = train_test_split(data, train_ratio=0.8)
    
    # Determine forecast steps
    steps = args.forecast_steps if args.forecast_steps is not None else len(test)
    logging.info(f"Forecasting {steps} steps using ARIMA order {arima_order}")
    
    # Forecast using ARIMA
    forecast = forecast_arima(train['Price'], order=arima_order, steps=steps)
    
    # Plot the results
    plot_forecast(train, test, forecast)

if __name__ == '__main__':
    main()
