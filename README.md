# Airline Operations Analytics Platform

Date: 26th Jan, 2026
This project was cleared by the course staff (R. Acuna) for public release on 5/22/2026.

This project was cleared by the course staff (R. Acuna) for public release on 5/22/2026.

Keywords: Airline operations, Route demand, Aircraft utilization

A data engineering and analytics platform for processing, warehousing, querying, and predicting U.S. domestic airline route utilization using BTS T-100 Domestic Segment data.

The system converts raw aviation operational data into analytics-ready Parquet files, loads curated tables into DuckDB, exposes route and aircraft intelligence through FastAPI endpoints, and provides ML-based load factor prediction using Scikit-learn.

<<<<<<< HEAD
Data Sourcing: The primary data source for this project is obtained from the Bureau of Transportation Statistics of the United States through the Department of Transportation's TranStats website. The data used for the analysis is the Form 41 Traffic dataset containing the T-100 Domestic Segment data, which contains operational data for U.S. carriers by route, including passenger data, available seats, number of departures made, aircraft types, carrier codes, and the time period. The data is obtained directly from the BTS website by selecting the data for U.S. domestic operations for the last year available. The data is then downloaded in CSV format for analysis. In order to better understand the data for the aircraft types variable, additional data is obtained from the BTS Aviation Support Tables to better understand the aircraft types by mapping the codes for aircraft types to the models of the aircraft. No datasets from Kaggle or any other sources are used for the project. In the absence of route profitability data, which is not publicly available, the load factor is used as a proxy for route profitability.
Dataset Source:
https://www.transtats.bts.gov/
Form 41 Traffic (T-100 Domestic Segment)

Data Provenance:
Dataset downloaded from BTS TranStats.
File hash verified locally.
=======
---
>>>>>>> portfolio-data-engineering-upgrade

## Tech Stack

<<<<<<< HEAD
Related Work: Prior academic research has examined airline route networks, capacity allocation, and aircraft utilization to better understand airline operational and deployment strategies. Existing studies have shown that passenger demand characteristics influence decisions related to flight frequency, aircraft size selection, and network structure, highlighting tradeoffs between utilization efficiency and network coverage. Other work has analyzed how airlines configure their networks over time in response to demand concentration and operational constraints, demonstrating that aircraft deployment patterns are closely tied to observed route-level demand. This project builds on such research by focusing on route-level operational patterns within U.S. domestic airline networks using publicly available data, without relying on proprietary financial or optimization models.

References:
1. Wei, W., Sun, X., & Wu, J. (2014).
Modeling airline passenger choice: Flight frequency, aircraft size, and network effects.
Transportation Research Part E: Logistics and Transportation Review, 67, 10–22.
2. Burghouwt, G., & de Wit, J. (2005).
Temporal configurations of airline networks in Europe.
Journal of Air Transport Management, 11(3), 185–198.

Pipeline Execution:
Run wf_core.py to execute full workflow.
=======
- Python
- Pandas
- NumPy
- DuckDB
- Parquet
- FastAPI
- Uvicorn
- Scikit-learn
- Matplotlib
- Docker
- Docker Compose

---

## Architecture

```text
Raw BTS T-100 CSV
        ↓
ETL Pipeline
        ↓
Data Validation + Quality Reporting
        ↓
Processed Parquet Dataset
        ↓
DuckDB Analytical Warehouse
        ↓
Warehouse Query Layer
        ↓
FastAPI Analytics + Prediction APIs
        ↓
Swagger/OpenAPI Documentation
```

---

## Key Features

- End-to-end ETL pipeline for large-scale airline operational data
- Data validation and data quality reporting
- Parquet-based processed dataset generation
- DuckDB warehouse with route-level and aircraft-level summary tables
- Warehouse query layer for route and aircraft intelligence
- FastAPI REST API with Swagger/OpenAPI documentation
- KNN-based load factor prediction endpoint
- Dockerized API deployment using Docker Compose
- Model benchmarking using MSE and R² score
- Route utilization, under-capacity, and aircraft utilization analytics

---

## Dataset

Source: U.S. Bureau of Transportation Statistics, T-100 Domestic Segment dataset.

The dataset includes U.S. domestic carrier route operations with passenger counts, available seats, departures performed, aircraft type, carrier information, and route identifiers.

No Kaggle datasets are used.

---

## Data Pipeline Outputs

The ETL pipeline produces:

- `data_processed/processed_data.parquet`
- `data_warehouse/airline_routes.duckdb`
- `logs/data_quality_report.txt`

Data quality report summary:

```text
Raw rows: 376,272
Clean rows: 342,025
Dropped rows: 34,247
Duplicate raw rows: 190
Rows with SEATS <= 0: 34,245
Rows with DEPARTURES_PERFORMED <= 0: 520
Rows with LOAD_FACTOR > 1.0: 41
```

---

## Warehouse Tables

The DuckDB warehouse contains:

- `clean_routes`
- `route_summary`
- `aircraft_summary`

Supported analytics:

- Top utilized routes
- Under-capacity routes
- Aircraft utilization by type
- Route lookup by airport pair

---

## Model Performance

Target variable: `LOAD_FACTOR`

| Model                      |      MSE |       R² |
| -------------------------- | -------: | -------: |
| Baseline Linear Regression | 0.073267 | 0.065651 |
| Main Linear Regression     | 0.048559 | 0.380746 |
| Ridge Regression           | 0.073267 | 0.065651 |
| Lasso Regression           | 0.053997 | 0.311393 |
| KNN Regressor              | 0.047077 | 0.399643 |

Best model: **KNN Regressor**

---

## API Endpoints

Open Swagger docs:

```text
http://127.0.0.1:8000/docs
```

Available endpoints:

```text
GET  /
GET  /health
GET  /routes/top-utilized
GET  /routes/under-capacity
GET  /aircraft/utilization
GET  /routes/{route}
POST /predict/load-factor
```

---

## Example Prediction Request

```json
{
  "seats": 13585,
  "departures_performed": 95,
  "aircraft_type": 612
}
```

## Example Prediction Response

```json
{
  "predicted_load_factor": 0.8237,
  "model_used": "KNN Regressor",
  "input": {
    "seats": 13585,
    "departures_performed": 95,
    "aircraft_type": 612
  }
}
```

---

## Run Locally

Create and activate a virtual environment:

```powershell
py -3.10 -m venv portfolio_venv
.\portfolio_venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the ETL pipeline:

```powershell
python pipeline\run_pipeline.py
```

Run the API:

```powershell
python -m uvicorn api.main:app --reload
```

Open Swagger docs:

```text
http://127.0.0.1:8000/docs
```

---

## Run with Docker

```powershell
docker compose up --build
```

Then open:

```text
http://127.0.0.1:8000/docs
```

---

## Project Structure

```text
api/
analytics/
pipeline/
data_original/
data_processed/
data_warehouse/
models/
evaluation/
visuals/
Dockerfile
docker-compose.yml
config.yaml
requirements.txt
```

---

## Future Improvements

- Add interactive dashboard for route analytics
- Add orchestration with Prefect or Airflow
- Add cloud deployment
- Add route distance and seasonal demand features
- Add data quality monitoring dashboard
>>>>>>> portfolio-data-engineering-upgrade
