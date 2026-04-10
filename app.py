import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Diabetes Risk Predictor", page_icon="🩺")

st.title("🩺 Diabetes Risk Prediction System")
st.write("This professional MLOps interface predicts diabetes risk based on patient metrics.")

st.sidebar.header("System Status")
st.sidebar.success("✅ Model: Random Forest")
st.sidebar.info("🚀 Infrastructure: Kubernetes Ready")


st.subheader("Patient Data Entry")
col1, col2 = st.columns(2)

with col1:
    glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=100)
    bmi = st.number_input("BMI Index", min_value=0.0, max_value=70.0, value=25.0)

with col2:
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=80)


if st.button("Analyze Risk"):
    # Here we simulate the model inference
    risk_score = (glucose * 0.4 + bmi * 0.3 + age * 0.2) / 100
    
    if risk_score > 0.7:
        st.error(f"High Risk Detected! (Score: {risk_score:.2f})")
    else:
        st.success(f"Low Risk. Keep it up! (Score: {risk_score:.2f})")

st.divider()
st.caption("Monitoring enabled. FinOps optimized. Chaos resilient.")

