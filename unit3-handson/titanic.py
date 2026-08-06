import pandas as pd
import matplotlib.pyplot as plt

# Read Titanic Dataset
df = pd.read_csv("data/titanic.csv")

print("========== TITANIC DATASET ==========\n")

# Display Dataset Information
print("\n========== DATASET INFORMATION ==========")
print(df.info())

# Missing Values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Descriptive Statistics
print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df.describe())

# Histogram (Age)
plt.figure(figsize=(6,4))
plt.hist(df["Age"].dropna(), bins=20, edgecolor="black")
plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Box Plot (Fare)
plt.figure(figsize=(5,6))
plt.boxplot(df["Fare"].dropna())
plt.title("Box Plot of Fare")
plt.ylabel("Fare")
plt.show()

# Detect Outliers using IQR (Fare)
Q1 = df["Fare"].quantile(0.25)
Q3 = df["Fare"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

outliers = df[(df["Fare"] < lower_limit) |
              (df["Fare"] > upper_limit)]

print("\n========== OUTLIERS ==========")
print(outliers[["Fare"]])

# Remove Outliers
cleaned_df = df[(df["Fare"] >= lower_limit) &
                (df["Fare"] <= upper_limit)]

print("\nOriginal Records :", len(df))
print("Records After Removing Outliers :", len(cleaned_df))

# Save Cleaned Dataset
cleaned_df.to_csv("Cleaned_Titanic.csv", index=False)

print("\nCleaned dataset saved as 'Cleaned_Titanic.csv'")