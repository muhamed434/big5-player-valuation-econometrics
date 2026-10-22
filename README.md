![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Framework](https://img.shields.io/badge/Econometrics-OLS-orange)
# Econometric Analysis of Market Value Drivers in Big-5 European Football

## Authors
* **Mukhamedzhan Kadir**
* **Yerkanat Manapuly**

## Research Questions & Overview
This research investigates the econometric drivers of football players' monetary market values across top-5 European leagues (EPL, La Liga, Serie A, Bundesliga, Ligue 1) using secondary performance and valuation datasets.

### Core Research Questions
* **RQ1 (Descriptive):** What are the key differences in market value distribution across player positions (defenders, midfielders, forwards)?
* **RQ2 (Causal/Non-linear):** How does age affect market value in a non-linear (parabolic) trajectory, and at what age is the peak valuation reached for different positions?
* **RQ3 (Comparative):** Do specialized position-specific metrics (e.g., tackles per 90, progressive passes per 90, xG per 90) explain market value variance better than aggregate goals/assists?

---

## Directory Structure

```text
big5-player-valuation-econometrics/
├── .gitignore               # Excludes python cache, virtual environments, and temporary logs
├── Dockerfile               # Reproducible containerization setup with fixed package pins
├── environment.yml          # Conda environment definition with strict version pins
├── LICENSE                  # Open source MIT license
├── README.md                # Project documentation and quickstart instructions
├── configs/
│   └── config.yaml          # Configuration file for independent variables and model parameters
├── data/
│   └── sample/
│       └── players_sample.csv # Micro dataset sample (8 players) for pipeline verification
├── docs/
│   └── methodology_passport.md # Methodology Passport Card
└── src/
    └── benchmark.py         # Executable benchmark code running OLS regression analysis
```

---

## Planned Benchmarks

| Model Specification | Target Sample | Explanatory Variables | Primary Metric (R²) | Guardrail Metric |
| :--- | :--- | :--- | :--- | :--- |
| **Baseline OLS** | All Positions | Age, Age², Goals+Assists/90, Minutes | R², Adjusted R² | VIF < 5.0 |
| **Defenders Model** | Defenders | Age, Age², Tackles/90, Interceptions/90 | Adjusted R², p-value | Breusch-Pagan p > 0.05 |
| **Midfielders Model** | Midfielders | Age, Age², Progressive Passes/90 | Adjusted R², p-value | Breusch-Pagan p > 0.05 |
| **Forwards Model** | Forwards | Age, Age², Expected Goals (xG)/90 | Adjusted R², p-value | Breusch-Pagan p > 0.05 |

---

## Quickstart Guide

You can launch and verify the econometric pipeline in 2–3 commands using Docker or Python / Conda.

### Option 1: Run via Docker (Recommended)

```bash
# 1. Build the Docker image
docker build -t big5-valuation-bench .

# 2. Execute the benchmark script on test data
docker run --rm big5-valuation-bench
```

### Option 2: Run via Conda / Python

```bash
# 1. Create and activate environment
conda env create -f environment.yml
conda activate big5-valuation

# 2. Run benchmark script
python src/benchmark.py
```

---

## License

This project is licensed under the terms of the MIT License.
## 🖥️ System Requirements

- **Operating System:** Linux / macOS / Windows 10+ (WSL2 recommended)
- **Python Version:** Python 3.10.13
- **Containerization:** Docker 24.0+ (Optional for containerized run)
- **Hardware:** Minimum 2 CPU cores, 4 GB RAM, 1 GB free disk space

## 📜 Citation

If you use this benchmark pipeline or methodology in your research, please cite our repository:

```bibtex
@misc{kadir2024big5valuation,
  author = {Kadir, Mukhamedzhan and Manapuly, Yerkanat},
  title = {Main factors affecting football players' market value in Big-5 European leagues: an econometric analysis by position groups},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{[https://github.com/muhamed434/big5-player-valuation-econometrics](https://github.com/muhamed434/big5-player-valuation-econometrics)}}
}
