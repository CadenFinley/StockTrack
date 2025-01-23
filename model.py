from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

def train_model(data_dict):
    models = {}
    for ticker, data in data_dict.items():
        X = data[['Open', 'High', 'Low', 'Volume']]
        y = data['Close'].values.ravel()  # Reshape y correctly
        
        if len(X) == 0 or len(y) == 0:
            print(f"Warning: Not enough data to train model for {ticker}")
            continue
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        
        print(f'{ticker} - Root Mean Squared Error: {rmse}')
        
        models[ticker] = model
    return models