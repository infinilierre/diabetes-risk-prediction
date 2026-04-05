# 🩺 Clinical Diabetes Risk Predictor (Monte Carlo Simulation)

This project is a **Medical Data Science** tool designed to predict Type 2 Diabetes risk using a machine learning approach. Since real patient data is private (GDPR/KVKK), I developed a **Monte Carlo Simulation** to create a realistic patient group and test clinical hypotheses.

## 🧠 Methodology: The Monte Carlo Approach
Instead of using fixed data, I used a **Monte Carlo simulation** with Python's NumPy to generate a synthetic cohort of **150 patients (n=150)**. 

* **Statistical Distribution:** The data follows **Normal Distributions** based on **NHANES** (National Health and Nutrition Examination Survey) standards:
    * **Glucose (Blood Sugar):** Average = 110 mg/dL, Standard Deviation = 20.
    * **BMI (Body Mass Index):** Average = 26, Standard Deviation = 4.
* **Biological Variance:** I intentionally avoided using a fixed "random seed". This allows the model to show **real-world randomness** in every run, meaning the results reflect different clinical realities each time.

## 🔬 Clinical Logic & Weighting
The model is inspired by the **FINDRISC** (Finnish Diabetes Risk Score) framework. The weights (w) in the code were calibrated to match medical evidence:
* **BMI Weight (0.10):** Selected as the primary driver due to its strong link to insulin resistance.
* **Glucose Weight (0.03):** Represents the acute metabolic state.
* **Age Weight (0.02):** Accounts for the biological decline of the pancreas over time.

## 📊 Key Insights: Feature Importance
The generated visualization (Bar Chart) identifies **BMI** as the most influential factor in the prediction. This validates the clinical hypothesis that lifestyle factors like weight are the most important predictors in early screening.

# 🛠️ Installation & Usage
1. Clone the repository:
   git clone https://github.com/infinilierre/diabetes-risk-predictor.git

2. Install dependencies:
   pip install -r requirements.txt

3. Run the simulation:
   python main.py
