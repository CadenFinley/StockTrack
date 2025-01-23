import numpy as np

def make_prediction(models, data_dict):
    predictions = {}
    for ticker, model in models.items():
        data = data_dict[ticker]
        X_new = data[['Open', 'High', 'Low', 'Volume']]
        predictions[ticker] = model.predict(X_new)
    return predictions