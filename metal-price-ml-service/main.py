from fastapi import FastAPI
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

app = FastAPI(title="Gold Silver ML Prediction API")

@app.get("/")
def home():
    return {"message": "ML Prediction API is running"}


@app.get("/predict/{metal}")
def predict_metal_price(metal: str):
    df = pd.read_csv("sample_data.csv")

    metal_df = df[df["metal"].str.lower() == metal.lower()].copy()

    if metal_df.empty:
        return {
            "metal": metal,
            "error": "No data found for this metal"
        }

    metal_df["day_number"] = np.arange(len(metal_df))

    X = metal_df[["day_number"]]
    y = metal_df["price"]

    model = LinearRegression()
    model.fit(X, y)

    next_day = [[len(metal_df)]]
    predicted_price = model.predict(next_day)[0]

    latest_price = metal_df["price"].iloc[-1]

    difference = predicted_price - latest_price
    change_percent = (difference / latest_price) * 100

    if change_percent > 0.3:
        trend = "UP"
    elif change_percent < -0.3:
        trend = "DOWN"
    else:
        trend = "STABLE"

    confidence = min(95, max(60, 70 + abs(change_percent) * 10))

    return {
        "metal": metal.capitalize(),
        "latestPrice": round(float(latest_price), 2),
        "predictedPrice": round(float(predicted_price), 2),
        "trend": trend,
        "changePercent": round(float(change_percent), 2),
        "confidence": round(float(confidence), 2),
        "model": "LinearRegression"
    }