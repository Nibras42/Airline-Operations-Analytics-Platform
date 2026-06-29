import duckdb


def save_parquet(df, path):
    df.to_parquet(path, index=False)


def load_to_duckdb(db_path, clean_df, route_summary_df, aircraft_summary_df, tables):
    con = duckdb.connect(db_path)

    con.register("clean_df", clean_df)
    con.register("route_summary_df", route_summary_df)
    con.register("aircraft_summary_df", aircraft_summary_df)

    con.execute(f"CREATE OR REPLACE TABLE {tables['clean_routes']} AS SELECT * FROM clean_df")
    con.execute(f"CREATE OR REPLACE TABLE {tables['route_summary']} AS SELECT * FROM route_summary_df")
    con.execute(f"CREATE OR REPLACE TABLE {tables['aircraft_summary']} AS SELECT * FROM aircraft_summary_df")

    con.close()