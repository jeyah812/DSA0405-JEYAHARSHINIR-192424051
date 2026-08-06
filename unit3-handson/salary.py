import pandas as pd
import matplotlib.pyplot as plt

# Read Salary Dataset
df = pd.read_csv("data/ds_salaries.csv")

# Display summary
print("========== SALARY DATA ==========\n")
print(df["salary_in_usd"].describe())

# Create Box Plot
plt.figure(figsize=(6,5))
plt.boxplot(df["salary_in_usd"], vert=True)

plt.title("Box Plot of Salary Data")
plt.ylabel("Salary (USD)")

plt.show()

# Detect Outliers using IQR
Q1 = df["salary_in_usd"].quantile(0.25)
Q3 = df["salary_in_usd"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

outliers = df[(df["salary_in_usd"] < lower_limit) |
              (df["salary_in_usd"] > upper_limit)]

print("\n========== OUTLIERS ==========")

if len(outliers) == 0:
    print("No outliers found.")
else:
    print(outliers[["salary_in_usd"]])

print("\nTotal Outliers:", len(outliers))