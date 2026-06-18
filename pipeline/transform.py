import pandas as pd


SELECTED_COLUMNS = [
    "YEAR",
    "MONTH",
    "UNIQUE_CARRIER",
    "UNIQUE_CARRIER_NAME",
    "ORIGIN_AIRPORT_ID",
    "ORIGIN",
    "DEST_AIRPORT_ID",
    "DEST",
    "AIRCRAFT_TYPE",
    "DEPARTURES_PERFORMED",
    "SEATS",
    "PASSENGERS",
]


def clean_airline_data(df):
    df = df[SELECTED_COLUMNS].copy()

    numeric_cols = [
        "YEAR",
        "MONTH",
        "ORIGIN_AIRPORT_ID",
        "DEST_AIRPORT_ID",
        "AIRCRAFT_TYPE",
        "DEPARTURES_PERFORMED",
        "SEATS",
        "PASSENGERS",
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=SELECTED_COLUMNS)
    df = df[(df["DEPARTURES_PERFORMED"] > 0) & (df["SEATS"] > 0)]

    df["ROUTE"] = df["ORIGIN"].astype(str) + "-" + df["DEST"].astype(str)
    df["LOAD_FACTOR"] = df["PASSENGERS"] / df["SEATS"]

    df = df[(df["LOAD_FACTOR"] >= 0) & (df["LOAD_FACTOR"] <= 1.5)]

    return df