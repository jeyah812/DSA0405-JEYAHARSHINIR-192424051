import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/sales_data4.csv")

plt.scatter(data["Month"], data["Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()