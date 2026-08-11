import pandas as pd
import matplotlib.pyplot as plt

# Read Iris Dataset
df = pd.read_csv("data/Iris.csv")

print("========== IRIS DATASET ==========\n")

# Dataset Information
print("\n========== DATASET INFORMATION ==========")
print(df.info())

# Missing Values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Descriptive Statistics
print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df.describe())

# Histogram
plt.figure(figsize=(7,5))
plt.hist(df["SepalLengthCm"], bins=15, edgecolor="black")
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# Box Plot
plt.figure(figsize=(5,6))
plt.boxplot(df["PetalLengthCm"])
plt.title("Box Plot of Petal Length")
plt.ylabel("Petal Length (cm)")
plt.show()

# Detect Outliers using IQR
Q1 = df["PetalLengthCm"].quantile(0.25)
Q3 = df["PetalLengthCm"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

outliers = df[
    (df["PetalLengthCm"] < lower_limit) |
    (df["PetalLengthCm"] > upper_limit)
]

print("\n========== OUTLIERS ==========")
print(outliers)

# Remove Outliers
cleaned_df = df[
    (df["PetalLengthCm"] >= lower_limit) &
    (df["PetalLengthCm"] <= upper_limit)
]

print("\nOriginal Records :", len(df))
print("Records After Removing Outliers :", len(cleaned_df))

# Save Cleaned Dataset
cleaned_df.to_csv("Cleaned_Iris.csv", index=False)

print("\nCleaned dataset saved as 'Cleaned_Iris.csv'")