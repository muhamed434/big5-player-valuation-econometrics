# Domain Model & Mathematical Specification (ML / Econometrics Track)

## 1. Mathematical Formulation

To resolve extreme right-skewness and heteroskedasticity in football transfer markets while ensuring robustness across positional tiers, we model the natural logarithm of market value with quadratic age dynamics and heteroskedasticity-consistent ($\text{HC1}$) covariance estimation, benchmarked against $L_2$-regularized and tree-ensemble estimators:

$$\ln(y_i) = \beta_0 + \sum_{k} \gamma_k \text{Position}_{ik} + \beta_1 \text{Age}_i + \beta_2 \text{Age}_i^2 + \mathbf{z}_i^\top \boldsymbol{\delta} + \mathbf{p}_i^\top \boldsymbol{\phi} + \varepsilon_i$$

For regularized benchmark comparisons, we minimize the $L_2$-penalized squared error objective on the log-transformed scale:

$$\min_{\boldsymbol{\theta}} \mathcal{L}(\boldsymbol{\theta}) = \frac{1}{N} \sum_{i=1}^{N} \left(\ln y_i - f(\mathbf{x}_i; \boldsymbol{\theta})\right)^2 + \lambda \|\boldsymbol{\theta}\|_2^2$$

---

## 2. Mathematical Notation Table

| Notation | Type | Domain Description |
| :--- | :--- | :--- |
| $N$ | Scalar | Total evaluated players with $\ge 90$ minutes played ($N = 1,200$: 431 Defenders, 407 Midfielders, 362 Forwards) |
| $\mathbf{x}_i \in \mathbb{R}^d$ | Vector | Full feature vector for player $i$ (Position, League, Club Tier, Age, Minutes, Contract Years, Position Metrics) |
| $\mathbf{z}_i$ | Vector | Control variables (`minutes_played`, `contract_years`, `club_tier`, `league`) |
| $\mathbf{p}_i$ | Vector | Position-specific performance metrics (`tackles_per90`, `prog_passes_per90`, `xg_per90`) |
| $y_i \in \mathbb{R}^+$ | Scalar | Observed market value in Euros (€) |
| $\hat{y}_i = \exp(f(\mathbf{x}_i; \boldsymbol{\theta}))$ | Scalar | Back-transformed model predicted market value (€) |
| $\lambda$ | Scalar | $L_2$ regularization penalty strength ($\lambda = 1.5$ for Ridge) |

---

## 3. Evaluation Metrics & Guardrail Specifications

- **Primary Valuation Metric:** Mean Absolute Error in Millions ($\text{MAE} = \frac{1}{N}\sum |y_i - \hat{y}_i| / 10^6$)
- **Tail-Sensitive Error Metric:** Root Mean Squared Error ($\text{RMSE} = \sqrt{\frac{1}{N}\sum (y_i - \hat{y}_i)^2} / 10^6$)
- **Goodness-of-Fit Metric:** Adjusted Coefficient of Determination ($\text{Adjusted } R^2$)
- **Multicollinearity Guardrail:** Variance Inflation Factor ($\text{VIF} < 5.0$ via mean-centered age terms)
