REQUIRED_COLUMNS = [
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


def validate_required_columns(df):
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def validate_row_count(df):
    if len(df) == 0:
        raise ValueError("Dataset is empty after loading.")