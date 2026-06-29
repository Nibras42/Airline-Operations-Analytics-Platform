import pickle
from pathlib import Path

import pandas as pd


MODEL_PATH = Path("models/knn_model.pkl")


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

    with open(MODEL_PATH, "rb") as file:
        return pickle.load(file)


def predict_load_factor(seats, departures_performed, aircraft_type):
    model = load_model()

    input_df = pd.DataFrame(
        {
            "SEATS": [float(seats)],
            "DEPARTURES_PERFORMED": [float(departures_performed)],
            "AIRCRAFT_TYPE": [int(aircraft_type)],
        },
        columns=["SEATS", "DEPARTURES_PERFORMED", "AIRCRAFT_TYPE"],
    )

    prediction = model.predict(input_df)[0]
    prediction = max(0.0, min(float(prediction), 1.5))

    return {
        "predicted_load_factor": round(prediction, 4),
        "model_used": "KNN Regressor",
        "input": {
            "seats": float(seats),
            "departures_performed": float(departures_performed),
            "aircraft_type": int(aircraft_type),
        },
    }