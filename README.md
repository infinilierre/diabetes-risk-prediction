# 🩺 Clinical Diabetes Risk Predictor (Monte Carlo Simulation)

This project is a **Medical Data Science** tool designed to predict Type 2 Diabetes risk using a stochastic machine learning approach. To address data privacy constraints (GDPR/KVKK), I implemented a **Monte Carlo Simulation** to generate synthetic cohorts and validate clinical hypotheses.

## 🧠 Methodology: The Monte Carlo Approach

Instead of relying on static datasets, the system generates a synthetic cohort ($n=150$) using **NumPy** to simulate realistic biological variance.

### Statistical Distribution
The data follows **Normal Distributions** calibrated according to **NHANES** (National Health and Nutrition Examination Survey) standards:
- **Glucose (Blood Sugar):** $\mu = 110$ mg/dL, $\sigma = 20$.
- **BMI (Body Mass Index):** $\mu = 26$, $\sigma = 4$.
- **Biological Variance:** By omitting a fixed random seed, the model captures real-world randomness, reflecting different clinical scenarios in every execution.

## 🔬 Clinical Logic & Weighting

Inspired by the **FINDRISC** framework, the prediction engine follows a weighted linear combination:
$$Risk = (w_1 \cdot BMI) + (w_2 \cdot Glucose) + (w_3 \cdot Age)$$

Where weights (w) are calibrated based on clinical evidence:
- **BMI (0.10):** Primary driver of insulin resistance.
- **Glucose (0.03):** Acute metabolic state indicator.
- **Age (0.02):** Biological pancreatic decline factor.

## 📊 Key Insights
The simulation identifies **BMI** as the most influential factor, validating the clinical hypothesis that lifestyle factors are the primary predictors in early screening.

## 🛠️ Installation
```powershell
git clone [https://github.com/infinilierre/diabetes-risk-predictor.git](https://github.com/infinilierre/diabetes-risk-predictor.git)
pip install -r requirements.txt
python main.py
