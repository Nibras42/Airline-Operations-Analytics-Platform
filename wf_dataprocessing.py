import os
import pandas as pd

ORIGINAL_PATH = os.path.join("data_original", "T_T100D_SEGMENT_US_CARRIER_ONLY.csv")
PROCESSED_DIR = "data_processed"
PROCESSED_PATH = os.path.join(PROCESSED_DIR, "processed_data.csv")


def load_raw_data(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Raw data file not found at: {path}\n"
            f"Make sure the CSV is in data_original/ and named correctly."
        )
    return pd.read_csv(path)


def process_data(df: pd.DataFrame):
    df.columns = [c.strip().upper() for c in df.columns]

    required_cols = [
        "YEAR", "MONTH",
        "UNIQUE_CARRIER", "UNIQUE_CARRIER_NAME",
        "ORIGIN_AIRPORT_ID", "ORIGIN",
        "DEST_AIRPORT_ID", "DEST",
        "AIRCRAFT_TYPE",
        "DEPARTURES_PERFORMED", "SEATS", "PASSENGERS"
    ]

    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df[required_cols].copy()

    numeric_cols = ["DEPARTURES_PERFORMED", "SEATS", "PASSENGERS", "YEAR", "MONTH"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["YEAR", "MONTH", "ORIGIN", "DEST", "AIRCRAFT_TYPE",
                           "DEPARTURES_PERFORMED", "SEATS", "PASSENGERS"])

    df = df[(df["DEPARTURES_PERFORMED"] > 0) & (df["SEATS"] > 0)]

    df["LOAD_FACTOR"] = df["PASSENGERS"] / df["SEATS"]

    df = df[(df["LOAD_FACTOR"] >= 0) & (df["LOAD_FACTOR"] <= 1.5)]

    return df


def save_processed_data(df: pd.DataFrame, path: str):
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    df.to_csv(path, index=False)


def main():
    df_raw = load_raw_data(ORIGINAL_PATH)
    df_processed = process_data(df_raw)
    save_processed_data(df_processed, PROCESSED_PATH)
    print(f"[wf_dataprocessing] Saved processed data to: {PROCESSED_PATH}")
    print(f"[wf_dataprocessing] Rows: {len(df_processed)}")


if __name__ == "__main__":
    main()