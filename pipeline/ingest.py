import pandas as pd


def load_raw_csv(path):
    return pd.read_csv(path)


def standardize_columns(df):
    df = df.copy()
    df.columns = [col.strip().upper() for col in df.columns]
    return df