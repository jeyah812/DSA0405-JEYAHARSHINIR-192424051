# ==========================================
# Fundamentals of Data Science
# Unit 2 - Data Preprocessing
# Experiment 1: Handling Missing Data
# ==========================================

import pandas as pd
import numpy as np

# Creating a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, 22],
    'Salary': [50000, 60000, np.nan, 45000]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display original dataset
print("Original DataFrame:\n")
print(df)

# Check for missing values
print("\nMissing Values Count:")
print(df.isnull().sum())

# Fill missing Age with the median value
df['Age'] = df['Age'].fillna(df['Age'].median())

# Remove rows where Salary is missing
df = df.dropna(subset=['Salary'])

# Display cleaned dataset
print("\nCleaned DataFrame:\n")
print(df)