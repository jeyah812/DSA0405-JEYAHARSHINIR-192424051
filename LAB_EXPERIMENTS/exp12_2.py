import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/weather_data.csv")

plt.scatter(data["Month"], data["Rainfall"])
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.show()