import duckdb


DB_PATH = "data_warehouse/airline_routes.duckdb"


def run_query(query):
    con = duckdb.connect(DB_PATH)
    result = con.execute(query).fetchdf()
    con.close()
    return result


def top_utilized_routes(limit=10):
    query = f"""
        SELECT
            route,
            origin,
            dest,
            total_passengers,
            total_seats,
            total_departures,
            ROUND(avg_load_factor, 4) AS avg_load_factor,
            aircraft_types
        FROM route_summary
        WHERE total_departures >= 10
        ORDER BY avg_load_factor DESC
        LIMIT {limit}
    """
    return run_query(query)


def under_capacity_routes(limit=10):
    query = f"""
        SELECT
            route,
            origin,
            dest,
            total_passengers,
            total_seats,
            route_capacity_gap,
            ROUND(avg_load_factor, 4) AS avg_load_factor
        FROM route_summary
        WHERE total_departures >= 10
        ORDER BY route_capacity_gap DESC
        LIMIT {limit}
    """
    return run_query(query)


def aircraft_utilization(limit=10):
    query = f"""
        SELECT
            aircraft_type,
            records,
            total_passengers,
            total_seats,
            unused_capacity,
            ROUND(avg_load_factor, 4) AS avg_load_factor,
            ROUND(avg_departures, 2) AS avg_departures
        FROM aircraft_summary
        ORDER BY records DESC
        LIMIT {limit}
    """
    return run_query(query)


def route_lookup(route):
    query = f"""
        SELECT *
        FROM route_summary
        WHERE route = '{route}'
    """
    return run_query(query)


def main():
    print("\nTop Utilized Routes")
    print(top_utilized_routes())

    print("\nUnder-Capacity Routes")
    print(under_capacity_routes())

    print("\nAircraft Utilization")
    print(aircraft_utilization())


if __name__ == "__main__":
    main()