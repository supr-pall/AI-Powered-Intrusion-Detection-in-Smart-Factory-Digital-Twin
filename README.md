# 🛡️ Smart Factory Digital Twin with AI Intrusion Detection

## 📌 Overview
This project simulates a **Smart Factory Digital Twin** and integrates an 
**AI-powered Intrusion Detection System (IDS)** to detect cyberattacks in IoT data.

## 🔄 Workflow
1. **IoT Data Simulation** → Generate normal + attack sensor data (`data_simulation.py`).
2. **AI Model Training** → Train anomaly detection model (`model_train.py`).
3. **Digital Twin Dashboard** → Visualize machine behavior + detect intrusions (`app.py`).

## 🛠️ Tech Stack
- Python
- Scikit-learn (Isolation Forest)
- Streamlit (Dashboard)
- Pandas, Numpy

## 🚀 How to Run
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Generate IoT data
python data_simulation.py

# 3. Train model
python model_train.py

# 4. Run Digital Twin Dashboard
streamlit run app.py
