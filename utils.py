# utils.py
import pandas as pd

def moving_average(series, window):
    """
    Calculate the moving average of a series.
    
    :param series: Pandas Series of values.
    :param window: Window size for moving average.
    :return: Pandas Series containing the moving average.
    """
    return series.rolling(window=window).mean()

def train_test_split(data, train_ratio=0.8):
    """
    Split data into training and testing sets.
    
    :param data: Pandas DataFrame with the dataset.
    :param train_ratio: Ratio of data to use for training.
    :return: Tuple (train, test) where each is a DataFrame.
    """
    split_idx = int(len(data) * train_ratio)
    train = data.iloc[:split_idx]
    test = data.iloc[split_idx:]
    return train, test
