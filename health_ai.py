import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


import warnings
warnings.filterwarnings('ignore') 
# 1. Dataset generation (Simulating medical data)
def create_data():
    # Glucose, BMI, Age and a simple outcome
    n = 150
    data = {
        'glucose': np.random.normal(110, 20, n),
        'bmi': np.random.normal(26, 4, n),
        'age': np.random.randint(20, 70, n)
    }
    df = pd.DataFrame(data)
    
    # Logic: Risk increases with glucose and BMI
    # Adding some random noise to make it realistic
    risk_score = (df['glucose'] * 0.03) + (df['bmi'] * 0.1) + (df['age'] * 0.02) - 8
    df['has_diabetes'] = (risk_score > np.random.normal(0, 1, n)).astype(int)
    return df

# 2. Main workflow
df = create_data()
X = df[['glucose', 'bmi', 'age']]
y = df['has_diabetes']

# Splitting data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training a simple Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Results
predictions = model.predict(X_test)
print(f"--- Diabetes Prediction Model ---")
print(f"Model Accuracy: {accuracy_score(y_test, predictions):.2f}")
print("\nDetailed Report:")
print(classification_report(y_test, predictions, zero_division=0))

# Testing a manual case
patient_data = pd.DataFrame([[140, 31, 50]], columns=['glucose', 'bmi', 'age'])
prob = model.predict_proba(patient_data)[0][1]
print(f"\nExample Patient Probability: {prob:.2%}")

# --- PERSONAL DATA INSIGHTS & VISUALIZATION ---
import matplotlib.pyplot as plt

# Mapping the features to their importance (Coefficients)
# This shows which medical factor has the most weight in our model
labels = ['Glucose Level', 'BMI Index', 'Patient Age']
importance = model.coef_[0]

print("\n[INFO] Generating clinical feature impact chart...")

# Creating the plot with custom colors to avoid that "generic" look
plt.figure(figsize=(9, 6))
colors = ['#ff7675', '#74b9ff', '#55efc4'] # Custom soft palette
plt.bar(labels, importance, color=colors, edgecolor='black', alpha=0.8)

# Adding a baseline and labels
plt.axhline(0, color='black', linewidth=1, linestyle='-')
plt.title('Diabetes Risk Factors: Feature Importance (McDaniel + ELTE)', fontsize=14, pad=20)
plt.xlabel('Medical Indicators', fontsize=12)
plt.ylabel('Weight in Model (Coefficients)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Adding a text note to show the manual logic
print(f"Analysis complete. Most influential factor: {labels[np.argmax(importance)]}")
print("Close the graph window to exit.")

plt.tight_layout()
plt.show()

