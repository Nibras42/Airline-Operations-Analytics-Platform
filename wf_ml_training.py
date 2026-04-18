import os
import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor

PROCESSED_PATH = os.path.join("data_processed", "processed_data.csv")
MODELS_DIR = "models"
TRAIN_PATH = os.path.join("data_processed", "train_data.csv")
TEST_PATH = os.path.join("data_processed", "test_data.csv")

TARGET = "LOAD_FACTOR"
BASELINE_FEATURES = ["SEATS"]
MAIN_FEATURES = ["SEATS", "DEPARTURES_PERFORMED", "AIRCRAFT_TYPE"]


def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Processed data file not found: {path}")
    return pd.read_csv(path)


def prepare_data(df):
    needed_cols = ["SEATS", "DEPARTURES_PERFORMED", "AIRCRAFT_TYPE", "LOAD_FACTOR"]
    df = df[needed_cols].dropna().copy()
    return df


def split_data(df):
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    return train_df, test_df


def save_split_data(train_df, test_df):
    train_df.to_csv(TRAIN_PATH, index=False)
    test_df.to_csv(TEST_PATH, index=False)


def train_baseline_model(train_df):
    X_train = train_df[BASELINE_FEATURES]
    y_train = train_df[TARGET]

    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def make_main_pipeline(model):
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), ["AIRCRAFT_TYPE"]),
            ("num", "passthrough", ["SEATS", "DEPARTURES_PERFORMED"])
        ]
    )

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    return pipeline


def train_main_model(train_df):
    X_train = train_df[MAIN_FEATURES]
    y_train = train_df[TARGET]

    model = make_main_pipeline(LinearRegression())
    model.fit(X_train, y_train)
    return model


def train_alternative_models(train_df):
    X_train = train_df[MAIN_FEATURES]
    y_train = train_df[TARGET]

    models = {
        "ridge_model.pkl": make_main_pipeline(Ridge(alpha=1.0)),
        "lasso_model.pkl": make_main_pipeline(Lasso(alpha=0.001, max_iter=5000)),
        "knn_model.pkl": make_main_pipeline(KNeighborsRegressor(n_neighbors=5))
    }

    for model in models.values():
        model.fit(X_train, y_train)

    return models


def save_model(model, filename):
    os.makedirs(MODELS_DIR, exist_ok=True)
    path = os.path.join(MODELS_DIR, filename)
    with open(path, "wb") as f:
        pickle.dump(model, f)


def main():
    df = load_data(PROCESSED_PATH)
    df = prepare_data(df)

    train_df, test_df = split_data(df)
    save_split_data(train_df, test_df)

    baseline_model = train_baseline_model(train_df)
    main_model = train_main_model(train_df)
    alternative_models = train_alternative_models(train_df)

    save_model(baseline_model, "baseline_model.pkl")
    save_model(main_model, "main_model.pkl")

    for filename, model in alternative_models.items():
        save_model(model, filename)

    print("[wf_ml_training] Training complete.")
    print(f"[wf_ml_training] Train rows: {len(train_df)}")
    print(f"[wf_ml_training] Test rows: {len(test_df)}")
    print("[wf_ml_training] Saved train/test split to data_processed/")
    print("[wf_ml_training] Saved models to models/")


if __name__ == "__main__":
    main()