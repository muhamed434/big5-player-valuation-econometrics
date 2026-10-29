import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cleaned_players_data.csv')

sns.set_theme(style="whitegrid", font_scale=1.1)
palette = sns.color_palette("colorblind")
pos_palette = {'Defender': palette[0], 'Midfielder': palette[1], 'Forward': palette[2]}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

sns.histplot(df['market_value'] / 1e6, kde=True, ax=ax1, color=palette[0], bins=30, edgecolor='white', alpha=0.7)
ax1.set_title('A: Raw Market Value Distribution (€ Millions)', fontsize=11, fontweight='bold')
ax1.set_xlabel('Market Value (EUR Millions)', fontsize=10, fontweight='bold')
ax1.set_ylabel('Player Count (Frequency)', fontsize=10, fontweight='bold')

sns.histplot(df['log_market_value'], kde=True, ax=ax2, color=palette[2], bins=30, edgecolor='white', alpha=0.7)
ax2.set_title('B: Log-Transformed Market Value ln(EUR)', fontsize=11, fontweight='bold')
ax2.set_xlabel('ln(Market Value in EUR)', fontsize=10, fontweight='bold')
ax2.set_ylabel('Player Count (Frequency)', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('mv_distribution.png', dpi=300)
plt.close()

fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x='position', y='log_market_value', palette=pos_palette, width=0.45, ax=ax)
sns.stripplot(data=df, x='position', y='log_market_value', color='black', alpha=0.2, jitter=0.2, size=3.5, ax=ax)
ax.set_title('Log Market Value Distribution Across Positions (RQ1)', fontsize=12, fontweight='bold')
ax.set_xlabel('Player Position Group', fontsize=11, fontweight='bold')
ax.set_ylabel('ln(Market Value in EUR)', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('position_boxplot.png', dpi=300)
plt.close()

g = sns.lmplot(
    data=df, x='age', y='log_market_value', hue='position', order=2, ci=95,
    palette=pos_palette, height=5, aspect=1.5,
    scatter_kws={'alpha': 0.3, 's': 25},
    line_kws={'linewidth': 2.5}
)
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Quadratic Age Trajectory Curves with 95% CI (RQ2)', fontsize=12, fontweight='bold')
g.set_axis_labels('Age (Years)', 'ln(Market Value in EUR)', fontsize=11, fontweight='bold')

plt.savefig('age_valuation_curves.png', dpi=300)
plt.close()

print("02: All 3 Scientific Plots generated and saved successfully!")
