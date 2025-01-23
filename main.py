
from data_loader import load_data, preprocess_data
from model import train_model
from predict import make_prediction

def main():
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2021-01-01'
    
    data = load_data(ticker, start_date, end_date)
    data = preprocess_data(data)
    
    model = train_model(data)
    
    predictions = make_prediction(model, data)
    print(predictions)

if __name__ == "__main__":
    main()