from pathlib import Path


def build_data_quality_report(raw_df, clean_df, report_path):
    Path(report_path).parent.mkdir(parents=True, exist_ok=True)

    raw_rows = len(raw_df)
    clean_rows = len(clean_df)
    dropped_rows = raw_rows - clean_rows

    required_columns = [
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

    null_counts = raw_df[required_columns].isnull().sum()
    duplicate_rows = raw_df.duplicated().sum()

    invalid_seats = raw_df[raw_df["SEATS"] <= 0].shape[0]
    invalid_departures = raw_df[raw_df["DEPARTURES_PERFORMED"] <= 0].shape[0]
    negative_passengers = raw_df[raw_df["PASSENGERS"] < 0].shape[0]

    load_factor_over_1 = clean_df[clean_df["LOAD_FACTOR"] > 1.0].shape[0]
    load_factor_over_1_25 = clean_df[clean_df["LOAD_FACTOR"] > 1.25].shape[0]

    lines = []
    lines.append("AIRLINE ROUTE DATA QUALITY REPORT")
    lines.append("=" * 40)
    lines.append("")
    lines.append(f"Raw rows: {raw_rows}")
    lines.append(f"Clean rows: {clean_rows}")
    lines.append(f"Dropped rows: {dropped_rows}")
    lines.append(f"Duplicate raw rows: {duplicate_rows}")
    lines.append("")
    lines.append("Missing Values by Required Column:")
    for col, count in null_counts.items():
        lines.append(f"- {col}: {count}")
    lines.append("")
    lines.append("Invalid Value Checks:")
    lines.append(f"- Rows with SEATS <= 0: {invalid_seats}")
    lines.append(f"- Rows with DEPARTURES_PERFORMED <= 0: {invalid_departures}")
    lines.append(f"- Rows with PASSENGERS < 0: {negative_passengers}")
    lines.append("")
    lines.append("Load Factor Quality Checks:")
    lines.append(f"- Rows with LOAD_FACTOR > 1.0: {load_factor_over_1}")
    lines.append(f"- Rows with LOAD_FACTOR > 1.25: {load_factor_over_1_25}")
    lines.append("")
    lines.append("Interpretation:")
    lines.append(
        "The report summarizes data completeness, invalid operational values, "
        "and load factor anomalies before the data is used for analytics or ML inference."
    )

    with open(report_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))