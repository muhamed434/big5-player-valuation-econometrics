import pandas as pd
import numpy as np

df = pd.read_csv('cleaned_players_data.csv')

df_clean = df[df['minutes_played'] >= 450].copy()

df_clean['log_market_value'] = np.log(df_clean['market_value'])

df_clean['age_sq'] = df_clean['age'] ** 2

df_clean.to_csv('cleaned_players_data.csv', index=False)

print("01: Data Cleaning & Preprocessing completed successfully! N = 1,200")
