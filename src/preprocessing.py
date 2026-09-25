"""
Data preprocessing
"""

import pandas as pd


def preprocess_data(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing numeric values
    numeric_cols = df.select_dtypes(include="number").columns

    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Convert date column
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    return df