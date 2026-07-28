import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/sales_data4.csv")

plt.plot(data["Month"], data["Sales"], marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()