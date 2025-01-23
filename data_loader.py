import yfinance as yf
import pandas as pd
import requests

def load_data(tickers, start_date, end_date):
    data_dict = {}
    for ticker in tickers:
        try:
            data = yf.download(ticker, start=start_date, end=end_date)
            if data.empty:
                print(f"Warning: No data found for {ticker}")
                continue
            data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
            data.dropna(inplace=True)
            data_dict[ticker] = data
        except Exception as e:
            print(f"Error downloading data for {ticker}: {e}")
    return data_dict

def preprocess_data(data):
    data['Return'] = data['Close'].pct_change()
    data.dropna(inplace=True)
    return data

def load_tickers():
    url = "https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/all/all_tickers.txt"
    response = requests.get(url)
    tickers = response.text.splitlines()
    
    # Get the 100 most expensive stocks
    prices = {}
    for ticker in tickers:
        try:
            data = yf.download(ticker, period='1d')
            if not data.empty:
                prices[ticker] = data['Close'].iloc[-1]
        except Exception as e:
            print(f"Error fetching price for {ticker}: {e}")
    
    sorted_tickers = sorted(prices, key=prices.get, reverse=True)[:100]
    return sorted_tickers
