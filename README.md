# StockTrack

StockTrack is a Python-based project that allows users to download stock data, preprocess it, train machine learning models, and make predictions on stock prices. The project uses Yahoo Finance for data retrieval and scikit-learn for machine learning.

## Features

- Load stock data from Yahoo Finance
- Preprocess the data by calculating returns
- Train machine learning models (Random Forest Regressor) on the data
- Make predictions on stock prices

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/cadenfinley/StockTrack.git
    cd StockTrack
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:
    ```sh
    python main.py
    ```

2. The script will:
    - Load the tickers of the 100 most expensive stocks
    - Download historical stock data for these tickers
    - Preprocess the data
    - Train machine learning models on the data
    - Make predictions on stock prices and print the latest prediction for each ticker

## Project Structure

- `data_loader.py`: Contains functions to load and preprocess stock data.
- `model.py`: Contains functions to train machine learning models.
- `predict.py`: Contains functions to make predictions using the trained models.
- `main.py`: The main script that ties everything together.

## Requirements

- Python 3.6+
- pandas
- numpy
- scikit-learn
- yfinance
- requests

## License

This project is licensed under the MIT License.