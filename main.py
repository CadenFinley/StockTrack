from data_loader import load_data, preprocess_data, load_tickers
from model import train_model
from predict import make_prediction

def main():
    tickers = load_tickers()
    start_date = '2020-01-01'
    end_date = '2021-01-01'
    
    data_dict = load_data(tickers, start_date, end_date)
    for ticker in tickers:
        if ticker in data_dict:
            data_dict[ticker] = preprocess_data(data_dict[ticker])
    
    models = train_model(data_dict)
    
    predictions = make_prediction(models, data_dict)
    for ticker, prediction in predictions.items():
        print(f'{ticker}: {prediction[-1]}')

if __name__ == "__main__":
    main()