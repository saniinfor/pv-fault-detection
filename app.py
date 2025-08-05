
import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("pv_fault_detector.pkl")

st.title("AI-Powered PV Fault Detection")

st.markdown("Enter the real-time PV system parameters below:")

voltage = st.number_input("Voltage (V)", min_value=0.0, value=35.0, step=0.1)
current = st.number_input("Current (A)", min_value=0.0, value=5.0, step=0.1)
temperature = st.number_input("Temperature (°C)", min_value=-10.0, value=40.0, step=0.5)
irradiance = st.number_input("Irradiance (W/m²)", min_value=0.0, value=800.0, step=10.0)

if st.button("Detect Fault"):
    input_data = np.array([[voltage, current, temperature, irradiance]])
    prediction = model.predict(input_data)
    st.success(f"Detected Fault Type: {prediction[0]}")
