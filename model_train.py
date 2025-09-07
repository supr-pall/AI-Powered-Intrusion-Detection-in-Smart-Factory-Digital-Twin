import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load simulated IoT data
data = pd.read_csv("iot_data.csv")

# Train Isolation Forest for anomaly detection
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(data)

# Save trained model
joblib.dump(model, "intrusion_model.pkl")

print("✅ Model trained and saved as intrusion_model.pkl")
