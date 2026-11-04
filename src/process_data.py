"""
Data processing and statistical aggregation module for player valuations.
"""

import numpy as np
import pandas as pd


def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """Loads raw dataset, filters cold-start noise, and applies log transformation."""
    df = pd.read_csv(file_path)

    # Filtering cold-start/noise (e.g. players with < 90 minutes played)
    if "minutes_played" in df.columns:
        df = df[df["minutes_played"] >= 90].copy()

    # Log Transformation for target market value
    if "market_value_eur" in df.columns:
        df["log_market_value"] = np.log(df["market_value_eur"])

    return df


def calculate_metrics_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates medians, percentiles, and statistical metrics by position."""
    if "position" not in df.columns or "market_value_eur" not in df.columns:
        return pd.DataFrame()

    summary = (
        df.groupby("position")["market_value_eur"]
        .agg(
            median="median",
            p25=lambda x: np.percentile(x, 25),
            p75=lambda x: np.percentile(x, 75),
            std="std",
        )
        .reset_index()
    )
    return summary
