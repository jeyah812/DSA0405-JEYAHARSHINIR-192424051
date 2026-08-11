import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Generate Raw Mock Data
raw_data = {
    "Employee_Name": [" Alice ", "Bob", "Charlie", "Diana", "Evan"],
    "Department": ["HR", "Engineering", "HR", "Engineering", "Marketing"],
    "Salary": [50000, 85000, np.nan, 92000, 60000],
    "Join_Date": [
        "2022-01-15",
        "2021-06-20",
        "2023-03-11",
        "2020-11-01",
        "2024-02-28"
    ]
}

df = pd.DataFrame(raw_data)

print("----- RAW DATA -----")
print(df)

# 2. Data Preprocessing

# Remove extra spaces
df["Employee_Name"] = df["Employee_Name"].str.strip()

# Replace missing salary with median
median_salary = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(median_salary)

# Convert Join_Date to datetime
df["Join_Date"] = pd.to_datetime(df["Join_Date"])

# Calculate Years of Service
df["Years_of_Service"] = 2026 - df["Join_Date"].dt.year

print("\n----- PREPROCESSED DATA -----")
print(df)

# 3. Data Aggregation
dept_summary = (
    df.groupby("Department")
      .agg(
          Avg_Salary=("Salary", "mean"),
          Total_Employees=("Employee_Name", "count")
      )
      .reset_index()
)

print("\n----- AGGREGATED SUMMARY -----")
print(dept_summary)

# 4. Data Visualization

sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar Chart
sns.barplot(
    data=dept_summary,
    x="Department",
    y="Avg_Salary",
    hue="Department",
    palette="Blues_d",
    legend=False,
    ax=axes[0]
)

axes[0].set_title("Average Salary by Department")
axes[0].set_xlabel("Department")
axes[0].set_ylabel("Salary ($)")

# Scatter Plot
sns.scatterplot(
    data=df,
    x="Years_of_Service",
    y="Salary",
    hue="Department",
    style="Department",
    s=200,
    ax=axes[1]
)

axes[1].set_title("Salary vs Years of Service")
axes[1].set_xlabel("Years of Service")
axes[1].set_ylabel("Salary ($)")

plt.tight_layout()
plt.show()