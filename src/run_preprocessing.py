import pandas as pd

from data_loader import load_data
from preprocessing import preprocess_data

portfolio, risk = load_data(
    "../data/raw/finsight_portfolio_data.csv",
    "../data/raw/finsight_risk_profiles.csv"
)

cleaned = preprocess_data(portfolio)

cleaned.to_csv(
    "../data/processed/cleaned_portfolio.csv",
    index=False
)

print("Cleaning completed!")
print(cleaned.head())