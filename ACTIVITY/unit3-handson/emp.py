import pandas as pd

# Read Employee Dataset
df = pd.read_csv("data/employee_data.csv")

print("========== EMPLOYEE DATASET ==========\n")
print(df.head())

print("\n========== DATASET SUMMARY ==========")

# Number of rows and columns
print("Number of Rows :", df.shape[0])
print("Number of Columns :", df.shape[1])

# Data Types
print("\nData Types:")
print(df.dtypes)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())