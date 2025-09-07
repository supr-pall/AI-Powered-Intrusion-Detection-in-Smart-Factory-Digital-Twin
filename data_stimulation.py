import numpy as np
import pandas as pd

# Simulate IoT machine data
np.random.seed(42)

# Normal machine behavior
normal_temp = np.random.normal(28, 2, 500)
normal_vib = np.random.normal(5, 1, 500)

# Simulated cyberattacks (false data injection)
attack_temp = np.random.choice([100, -20, 200], 20)
attack_vib = np.random.choice([300, 800, 1000], 20)

# Merge normal + attack data
temp = np.concatenate([normal_temp, attack_temp])
vib = np.concatenate([normal_vib, attack_vib])

data = pd.DataFrame({"temp": temp, "vibration": vib})
data.to_csv("iot_data.csv", index=False)

print("✅ IoT data with attacks saved to iot_data.csv")
