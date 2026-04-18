import os
import pickle
import pandas as pd

TEST_PATH = os.path.join("data_processed", "test_data.csv")
MODELS_DIR = "models"

TARGET = "LOAD_FACTOR"
BASELINE_FEATURES = ["SEATS"]
MAIN_FEATURES = ["SEATS", "DEPARTURES_PERFORMED", "AIRCRAFT_TYPE"]


def load_test_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Test data file not found: {path}")
    return pd.read_csv(path)


def load_model(model_filename):
    model_path = os.path.join(MODELS_DIR, model_filename)
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model


def predict_with_model(model, test_df, feature_type="main"):
    if feature_type == "baseline":
        X_test = test_df[BASELINE_FEATURES]
    else:
        X_test = test_df[MAIN_FEATURES]

    predictions = model.predict(X_test)
    return predictions


def main():
    test_df = load_test_data(TEST_PATH)

    baseline_model = load_model("baseline_model.pkl")
    main_model = load_model("main_model.pkl")

    baseline_predictions = predict_with_model(baseline_model, test_df, feature_type="baseline")
    main_predictions = predict_with_model(main_model, test_df, feature_type="main")

    print("[wf_ml_prediction] Prediction complete.")
    print(f"[wf_ml_prediction] Baseline predictions: {len(baseline_predictions)}")
    print(f"[wf_ml_prediction] Main model predictions: {len(main_predictions)}")


if __name__ == "__main__":
    main()