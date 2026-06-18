import logging
from pathlib import Path

import yaml

from ingest import load_raw_csv, standardize_columns
from validate import validate_required_columns, validate_row_count
from transform import clean_airline_data
from aggregate import build_route_summary, build_aircraft_summary
from load import save_parquet, load_to_duckdb
from data_quality import build_data_quality_report


def load_config():
    with open("config.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def setup_logging(log_path):
    Path(log_path).parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def ensure_directories(config):
    for key in ["processed_parquet", "warehouse_db", "pipeline_log"]:
        Path(config["paths"][key]).parent.mkdir(parents=True, exist_ok=True)


def main():
    config = load_config()
    ensure_directories(config)
    setup_logging(config["paths"]["pipeline_log"])

    logging.info("Starting airline route ETL pipeline.")

    raw_df = load_raw_csv(config["paths"]["raw_csv"])
    logging.info("Loaded raw dataset with %s rows.", len(raw_df))

    raw_df = standardize_columns(raw_df)
    validate_required_columns(raw_df)
    validate_row_count(raw_df)
    
    clean_df = clean_airline_data(raw_df)
    logging.info("Cleaned dataset contains %s rows.", len(clean_df))

    build_data_quality_report(
        raw_df,
        clean_df,
        config["paths"]["data_quality_report"],
    )
    logging.info("Cleaned dataset contains %s rows.", len(clean_df))

    route_summary_df = build_route_summary(clean_df)
    aircraft_summary_df = build_aircraft_summary(clean_df)

    save_parquet(clean_df, config["paths"]["processed_parquet"])
    load_to_duckdb(
        config["paths"]["warehouse_db"],
        clean_df,
        route_summary_df,
        aircraft_summary_df,
        config["tables"],
    )

    logging.info("Saved parquet and loaded DuckDB warehouse.")
    print("[pipeline] ETL complete.")
    print(f"[pipeline] Clean rows: {len(clean_df)}")
    print(f"[pipeline] Route summary rows: {len(route_summary_df)}")
    print(f"[pipeline] Aircraft summary rows: {len(aircraft_summary_df)}")


if __name__ == "__main__":
    main()