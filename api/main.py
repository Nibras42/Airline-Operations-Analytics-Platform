from pydantic import BaseModel, Field
from api.prediction_service import predict_load_factor
from fastapi import FastAPI
from analytics.warehouse_queries import (
    top_utilized_routes,
    under_capacity_routes,
    aircraft_utilization,
    route_lookup,
)

app = FastAPI(
    title="Airline Route Intelligence API",
    description="Analytics and ML-ready aviation data platform built on BTS T-100 data.",
    version="1.0.0",
)

class LoadFactorPredictionRequest(BaseModel):
    seats: float = Field(..., gt=0)
    departures_performed: float = Field(..., gt=0)
    aircraft_type: int = Field(..., gt=0)


@app.get("/")
def root():
    return {
        "message": "Airline Route Intelligence API is running."
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/routes/top-utilized")
def get_top_utilized_routes(limit: int = 10):
    result = top_utilized_routes(limit)
    return result.to_dict(orient="records")


@app.get("/routes/under-capacity")
def get_under_capacity_routes(limit: int = 10):
    result = under_capacity_routes(limit)
    return result.to_dict(orient="records")


@app.get("/aircraft/utilization")
def get_aircraft_utilization(limit: int = 10):
    result = aircraft_utilization(limit)
    return result.to_dict(orient="records")


@app.get("/routes/{route}")
def get_route(route: str):
    result = route_lookup(route)

    if result.empty:
        return {
            "message": f"No data found for route {route}"
        }

    return result.to_dict(orient="records")

@app.post("/predict/load-factor")
def predict_route_load_factor(request: LoadFactorPredictionRequest):
    return predict_load_factor(
        seats=request.seats,
        departures_performed=request.departures_performed,
        aircraft_type=request.aircraft_type,
    )