
import numpy as np

def make_prediction(model, data):
    X_new = data[['Open', 'High', 'Low', 'Volume']]
    predictions = model.predict(X_new)
    return predictions