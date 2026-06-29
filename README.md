# Airline Operations Analytics Platform

Date: 26th Jan, 2026
This project was cleared by the course staff (R. Acuna) for public release on 5/22/2026.

Keywords: Airline operations, Route demand, Aircraft utilization

A data engineering and analytics platform for processing, warehousing, querying, and predicting U.S. domestic airline route utilization using BTS T-100 Domestic Segment data.

The system converts raw aviation operational data into analytics-ready Parquet files, loads curated tables into DuckDB, exposes route and aircraft intelligence through FastAPI endpoints, and provides ML-based load factor prediction using Scikit-learn.

---

## Tech Stack

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
