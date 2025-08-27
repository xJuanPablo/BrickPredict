import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "kc_house_data.csv")

data = pd.read_csv(data_path)

x = data[['sqft_living', 'bedrooms', 'bathrooms', 'condition']]
y = data['price']

model = LinearRegression()
model.fit(x, y)

model_path = os.path.join(BASE_DIR, "app", "model.pkl")
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")