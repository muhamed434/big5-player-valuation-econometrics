import numpy as np
import pandas as pd


def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """Loads raw dataset, filters low-minute noise, and applies log transformation."""
    df = pd.read_csv(file_path)

    if "minutes_played" in df.columns:
        df = df[df["minutes_played"] >= 90].copy()

    if "market_value" in df.columns:
        df = df[df["market_value"] > 0].copy()
        df["log_market_value"] = np.log(df["market_value"])

    df["age_centered"] = df["age"] - df["age"].mean()
    df["age_sq"] = df["age"] ** 2
    df["age_centered_sq"] = df["age_centered"] ** 2
    return df


def calculate_metrics_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates medians, percentiles, and statistical metrics by position."""
    summary = (
        df.groupby("position")["market_value"]
        .agg(
            player_count="count",
            mean="mean",
            median="median",
            p25=lambda x: np.percentile(x, 25),
            p75=lambda x: np.percentile(x, 75),
            std="std",
        )
        .reset_index()
    )
    return summary
