import pandas as pd
import streamlit as st
import joblib

# Load data + model
data = pd.read_csv("iot_data.csv")
model = joblib.load("intrusion_model.pkl")

# Predict anomalies
data["anomaly"] = model.predict(data)  # -1 = anomaly, 1 = normal
attack_points = data[data["anomaly"] == -1]

# Streamlit Dashboard
st.title("🛡️ Smart Factory Digital Twin with AI Intrusion Detection")

st.subheader("📊 Machine Data")
st.line_chart(data[["temp", "vibration"]])

st.subheader("⚠️ Detected Anomalies")
st.write(attack_points)

# Log anomalies
attack_points.to_csv("attack_log.csv", index=False)
st.success("Attack log saved as attack_log.csv")
