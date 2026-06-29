def build_route_summary(df):
    summary = (
        df.groupby(["ROUTE", "ORIGIN", "DEST"], as_index=False)
        .agg(
            total_passengers=("PASSENGERS", "sum"),
            total_seats=("SEATS", "sum"),
            total_departures=("DEPARTURES_PERFORMED", "sum"),
            avg_load_factor=("LOAD_FACTOR", "mean"),
            aircraft_types=("AIRCRAFT_TYPE", "nunique"),
        )
    )

    summary["route_capacity_gap"] = summary["total_seats"] - summary["total_passengers"]
    return summary


def build_aircraft_summary(df):
    summary = (
        df.groupby("AIRCRAFT_TYPE", as_index=False)
        .agg(
            records=("AIRCRAFT_TYPE", "count"),
            total_passengers=("PASSENGERS", "sum"),
            total_seats=("SEATS", "sum"),
            avg_load_factor=("LOAD_FACTOR", "mean"),
            avg_departures=("DEPARTURES_PERFORMED", "mean"),
        )
    )

    summary["unused_capacity"] = summary["total_seats"] - summary["total_passengers"]
    return summary