"""
Module: data_loader.py

Purpose:
Load portfolio and risk profile datasets.
"""

import pandas as pd


def load_data(portfolio_path, risk_profile_path):
    """
    Load portfolio and risk profile datasets.
    """

    portfolio_df = pd.read_csv(portfolio_path)
    risk_df = pd.read_csv(risk_profile_path)

    return portfolio_df, risk_df