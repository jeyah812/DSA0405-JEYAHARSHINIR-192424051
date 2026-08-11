# ==========================================
# Fundamentals of Data Science
# Unit 2 - Data Preprocessing
# Experiment 4: Using describe()
# ==========================================

import pandas as pd

# Creating a sample dataset
data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 75000, 90000, 110000],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'HR']
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display original dataset
print("Original DataFrame:\n")
print(df)

# Summary of numeric columns
print("\n--- Numeric Summary ---")
print(df.describe())

# Summary of categorical columns
print("\n--- Categorical Summary ---")
print(df.describe(include='object'))