import yfinance as yf
import pandas as pd

def load_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    data.dropna(inplace=True)
    return data

def preprocess_data(data):
    data['Return'] = data['Close'].pct_change()
    data.dropna(inplace=True)
    return data
