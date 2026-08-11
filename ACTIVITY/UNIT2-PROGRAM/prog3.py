# ==========================================
# Fundamentals of Data Science
# Unit 2 - Data Preprocessing
# Experiment 3: Aggregating and Grouping Data
# ==========================================

import pandas as pd

# Creating a sample dataset
data = {
    'Store': ['North', 'South', 'North', 'West', 'South', 'West'],
    'Sales': [1200, 1500, 900, 1100, 1700, 1300],
    'Employees': [5, 7, 5, 4, 8, 4]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display original dataset
print("Original DataFrame:\n")
print(df)

# Group by Store and calculate total sales and average employees
summary = df.groupby('Store').agg({
    'Sales': 'sum',
    'Employees': 'mean'
}).reset_index()

# Display summary
print("\nGrouped Summary:\n")
print(summary)