# utils.py
import pandas as pd

def moving_average(series, window):
    """Calculate the moving average of a series."""
    return series.rolling(window=window).mean()

def train_test_split(data, train_ratio=0.8):
    """Split data into training and testing sets."""
    split_idx = int(len(data) * train_ratio)
    train = data.iloc[:split_idx]
    test = data.iloc[split_idx:]
    return train, test
