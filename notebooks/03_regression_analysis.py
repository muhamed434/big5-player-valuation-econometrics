import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.diagnostic import het_breuschpagan

df = pd.read_csv('cleaned_players_data.csv')
df['age_sq'] = df['age'] ** 2

m1 = smf.ols('log_market_value ~ age + age_sq + minutes_played + contract_years', data=df).fit(cov_type='HC1')

m2 = smf.ols('log_market_value ~ age + age_sq + minutes_played + contract_years + C(position, Treatment("Defender"))', data=df).fit(cov_type='HC1')

m3 = smf.ols('log_market_value ~ age + age_sq + minutes_played + contract_years + C(position, Treatment("Defender")) + xg_per90 + prog_passes_per90 + tackles_per90', data=df).fit(cov_type='HC1')

print("=== MODEL 1 SUMMARY ===")
print(m1.summary().tables[1])
print(f"Model 1 Adjusted R2: {m1.rsquared_adj:.4f}\n")

print("=== MODEL 2 SUMMARY (RQ1 & RQ2) ===")
print(m2.summary().tables[1])
print(f"Model 2 Adjusted R2: {m2.rsquared_adj:.4f}\n")

print("=== MODEL 3 SUMMARY (RQ3) ===")
print(m3.summary().tables[1])
print(f"Model 3 Adjusted R2: {m3.rsquared_adj:.4f}\n")

bp_test = het_breuschpagan(m2.resid, m2.model.exog)
print(f"Breusch-Pagan LM Stat: {bp_test[0]:.2f}, p-value: {bp_test[1]:.4f}")
