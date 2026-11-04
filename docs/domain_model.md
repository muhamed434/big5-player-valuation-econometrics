# Domain Model & Mathematical Specification (ML / Econometrics Track)

## 1. Mathematical Formulation

To resolve extreme value distortions (outliers) in football transfer markets while ensuring robustness across average player valuations, we apply a **Log-Huber Loss** optimization criterion combined with $L_2$ regularization:

$$\min_{\boldsymbol{\theta}} \mathcal{L}(\boldsymbol{\theta}) = \frac{1}{N} \sum_{i=1}^{N} L_{\delta}(y_i, f(\mathbf{x}_i; \boldsymbol{\theta})) + \lambda \|\boldsymbol{\theta}\|_2^2$$

Where $L_{\delta}(y_i, \hat{y}_i)$ is mathematically defined as:

$$L_{\delta}(y_i, \hat{y}_i) = \begin{cases} \frac{1}{2}\left(\ln y_i - \ln \hat{y}_i\right)^2 & \text{if } |\ln y_i - \ln \hat{y}_i| \le \delta \\ \delta \cdot |\ln y_i - \ln \hat{y}_i| - \frac{1}{2}\delta^2 & \text{otherwise} \end{cases}$$

---

## 2. Mathematical Notation Table

| Notation | Type | Domain Description |
| :--- | :--- | :--- |
| $N$ | Scalar | Total number of evaluated players ($N = 1,200$) |
| $\mathbf{x}_i \in \mathbb{R}^d$ | Vector | Feature vector for player $i$ (Age, xG, xA, Minutes, Position) |
| $y_i \in \mathbb{R}^+$ | Scalar | Observed market value in Euros (€) |
| $\hat{y}_i = f(\mathbf{x}_i; \boldsymbol{\theta})$ | Scalar | Model predicted market value |
| $\boldsymbol{\theta}$ | Vector | Model parameters / weights |
| $\delta$ | Scalar | Huber threshold parameter separating quadratic and linear loss |
| $\lambda$ | Scalar | $L_2$ regularization penalty strength |

---

## 3. Evaluation Metrics & Target Specifications

- **Primary Valuation Metric:** Mean Absolute Error ($\text{MAE} = \frac{1}{N}\sum |y_i - \hat{y}_i|$)
- **Goodness-of-Fit Metric:** Coefficient of Determination ($R^2$)
- **Guardrail Metric:** Mean Absolute Percentage Error ($\text{MAPE} \le 18.0\%$)
