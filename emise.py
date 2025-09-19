#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

# Data o emisích CO₂
data = {
    "Doprava": ["Letadlo", "Auto (benzín)", "Auto (elektrické)", "Vlak", "Autobus", "Kolo"],
    "CO2 na 1 km (kg)": [0.255, 0.192, 0.060, 0.041, 0.105, 0.0]
}

df = pd.DataFrame(data)
df["Vzdálenost (km)"] = 1000
df["Celkem CO2 (kg)"] = df["CO2 na 1 km (kg)"] * df["Vzdálenost (km)"]

# Zobrazení výsledků
print(df[["Doprava", "Celkem CO2 (kg)"]])

# Vykreslení grafu
plt.figure(figsize=(10,6))
plt.bar(df["Doprava"], df["Celkem CO2 (kg)"], color='navy')
plt.title("CO₂ emise na 1000 km podle způsobu dopravy")
plt.ylabel("CO₂ (kg)")
plt.xlabel("Doprava")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

