import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Read dataset
df = pd.read_csv("data/age_bodyfat.csv")

print("========== AGE AND BODY FAT DATA ==========\n")
print(df)

# Statistical Summary
print("\n========== STATISTICAL SUMMARY ==========")

print("\nAge:")
print("Mean :", round(df["Age"].mean(), 2))
print("Median :", round(df["Age"].median(), 2))
print("Standard Deviation :", round(df["Age"].std(), 2))

print("\nBody Fat (%):")
print("Mean :", round(df["Body_Fat"].mean(), 2))
print("Median :", round(df["Body_Fat"].median(), 2))
print("Standard Deviation :", round(df["Body_Fat"].std(), 2))

# Box Plots
plt.figure(figsize=(7, 5))
plt.boxplot([df["Age"], df["Body_Fat"]], labels=["Age", "Body Fat %"])
plt.title("Box Plots of Age and Body Fat")
plt.ylabel("Values")
plt.show()

# Scatter Plot
plt.figure(figsize=(7, 5))
plt.scatter(df["Age"], df["Body_Fat"])
plt.title("Age vs Body Fat Percentage")
plt.xlabel("Age")
plt.ylabel("Body Fat (%)")
plt.grid(True)
plt.show()

# Q-Q Plot for Age
plt.figure(figsize=(6, 5))
stats.probplot(df["Age"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")
plt.show()

# Q-Q Plot for Body Fat
plt.figure(figsize=(6, 5))
stats.probplot(df["Body_Fat"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Body Fat Percentage")
plt.show()