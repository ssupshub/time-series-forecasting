# main.py
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from utils import train_test_split

def load_data(file_path):
    """
    Load the CSV file containing stock data.
    Expects a 'Date' column and a 'Price' column.
    """
    try:
        data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    except Exception as e:
        print(f"Error loading data: {e}")
        raise
    return data

def forecast_arima(train, order=(5,1,0), steps=30):
    """
    Build and forecast the ARIMA model.
    :param train: Training data (a pandas Series).
    :param order: ARIMA model order (p,d,q).
    :param steps: Number of future steps to forecast.
    :return: Forecasted values as a pandas Series.
    """
    try:
        model = ARIMA(train, order=order)
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=steps)
    except Exception as e:
        print(f"Error during ARIMA model fitting or forecasting: {e}")
        raise
    return forecast

def main():
    # Load the sample stock data CSV file
    file_path = 'stock_data.csv'
    data = load_data(file_path)
    
    # Split data into training and testing sets
    train, test = train_test_split(data, train_ratio=0.8)
    
    # Forecast for the length of the test set
    forecast = forecast_arima(train['Price'], steps=len(test))
    
    # Plot the training data, test data, and forecasted values
    plt.figure(figsize=(12,6))
    plt.plot(train.index, train['Price'], label='Training Data')
    plt.plot(test.index, test['Price'], label='Test Data')
    plt.plot(test.index, forecast, label='Forecast', color='red', linestyle='--')
    plt.title("Time Series Forecasting using ARIMA")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
