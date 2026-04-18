import os
import pickle
import pandas as pd

from sklearn.metrics import mean_squared_error, r2_score

TEST_PATH = os.path.join("data_processed", "test_data.csv")
MODELS_DIR = "models"
EVAL_DIR = "evaluation"
SUMMARY_PATH = os.path.join(EVAL_DIR, "summary.txt")

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


def evaluate_model(model, test_df, feature_type="main"):
    if feature_type == "baseline":
        X_test = test_df[BASELINE_FEATURES]
    else:
        X_test = test_df[MAIN_FEATURES]

    y_test = test_df[TARGET]
    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    return mse, r2


def write_summary(results):
    os.makedirs(EVAL_DIR, exist_ok=True)

    lines = []
    lines.append("MODEL EVALUATION SUMMARY\n")
    lines.append(f"{'Model':<20} {'MSE':<20} {'R2':<20}")

    for model_name, metrics in results.items():
        mse, r2 = metrics
        lines.append(f"{model_name:<20} {mse:<20.6f} {r2:<20.6f}")

    with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[wf_ml_evaluation] Wrote evaluation summary to: {SUMMARY_PATH}")


def main():
    test_df = load_test_data(TEST_PATH)

    results = {}

    baseline_model = load_model("baseline_model.pkl")
    results["Baseline"] = evaluate_model(baseline_model, test_df, feature_type="baseline")

    main_model = load_model("main_model.pkl")
    results["Main_Linear"] = evaluate_model(main_model, test_df, feature_type="main")

    ridge_model = load_model("ridge_model.pkl")
    results["Ridge"] = evaluate_model(ridge_model, test_df, feature_type="main")

    lasso_model = load_model("lasso_model.pkl")
    results["Lasso"] = evaluate_model(lasso_model, test_df, feature_type="main")

    knn_model = load_model("knn_model.pkl")
    results["KNN"] = evaluate_model(knn_model, test_df, feature_type="main")

    write_summary(results)

    print("[wf_ml_evaluation] Evaluation complete.")
    for name, (mse, r2) in results.items():
        print(f"{name}: MSE={mse:.6f}, R2={r2:.6f}")


if __name__ == "__main__":
    main()