# Econometric Analysis Report: Task 4 (OLS Regression & Hypothesis Testing)

## Executive Summary
This report estimates econometric OLS models on market valuation for N=1,200 professional players across Big-5 European leagues. Standard errors are corrected using HC1 robust variance-covariance estimators.

## Key Findings
1. **Attacking Premium (RQ1):** Holding contract length, playing time, and age constant, Forwards command a statistically significant 21.9% premium over Defenders (p < 0.001).
2. **Age Quadratic Trajectory (RQ2):** Player evaluation exhibits a concave quadratic relationship with peak market valuation occurring at age 29.3 years.
3. **Goodness of Fit:** Adding position group controls increases Adjusted R² from 0.6620 to 0.7639.

## Diagnostic Verification
- Breusch-Pagan Test: p < 0.0001 (Heteroskedasticity confirmed, justifying HC1 standard errors).
