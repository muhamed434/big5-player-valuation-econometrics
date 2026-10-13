# Data Directory Overview

This directory contains data assets used for the econometric evaluation of European football players' market values.

## Directory Structure

* `sample/players_sample.csv`: Micro dataset sample (8 players) included in version control for automated pipeline verification and baseline testing.
* `raw/` *(Gitignored)*: Location for full secondary datasets downloaded/scraped from FBref/StatsBomb and Transfermarkt.
* `processed/` *(Gitignored)*: Transformed, position-segmented, and log-transformed data prepared for regression estimation.

## Data Setup Instructions

1. For test runs, the pipeline automatically uses `data/sample/players_sample.csv`.
2. For full econometric model replication, place your extracted raw dataset into `data/raw/players_raw.csv`.
3. Executing `src/benchmark.py` will process and output model metrics based on the active dataset configuration in `configs/config.yaml`.

*Note: Large raw data files are intentionally excluded from Git tracking via `.gitignore`.*
