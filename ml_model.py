import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

def train_spending_model():
    
    transactions = get_transactions()
    
    
    df = pd.DataFrame(transactions, columns=['id', 'account_id', 'amount', 'date', 'category'])
    
    
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    
    
    X = df[['month']]
    y = df['amount']
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
   
    predictions = model.predict(X_test)
    error = np.sqrt(mean_squared_error(y_test, predictions))
    print(f'Prediction RMSE: {error}')
    
    return model


train_spending_model()
