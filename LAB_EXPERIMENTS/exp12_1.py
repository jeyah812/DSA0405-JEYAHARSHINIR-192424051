import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/weather_data.csv")

plt.plot(data["Month"], data["Temperature"], marker='o')
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()