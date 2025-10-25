import os
import pandas as pd
from src.forecast_model import train_forecast
from src.visualization import plot_approval_vs_delay

base = os.path.dirname(__file__)
data_path = os.path.join(base, 'data', 'procurement_data.csv')
results_path = os.path.join(base, 'dashboard','screenshots')
os.makedirs(results_path, exist_ok=True)
model_path = os.path.join(base, 'dashboard','procurement_delay_model.joblib')
plot_path = os.path.join(results_path, 'approval_vs_delay.png')

df = pd.read_csv(data_path)
model = train_forecast(df, model_path)
plot_approval_vs_delay(df, plot_path)
print('Procurement project complete. Outputs in', results_path)
