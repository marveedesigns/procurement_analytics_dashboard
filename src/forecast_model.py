from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

def train_forecast(df, model_path):
    X = df[['po_amount', 'approval_time_days']]
    y = df['delay_days']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print('MSE:', mean_squared_error(y_test, preds))
    joblib.dump(model, model_path)
    return model
