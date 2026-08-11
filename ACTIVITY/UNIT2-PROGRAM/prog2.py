# ==========================================
# Fundamentals of Data Science
# Unit 2 - Data Preprocessing
# Experiment 2: Filtering Rows Based on Multiple Conditions
# ==========================================

import pandas as pd

# Creating a sample dataset
data = {
    'Employee': ['Amy', 'John', 'Raj', 'Kevin', 'Sora'],
    'Department': ['HR', 'IT', 'IT', 'Sales', 'IT'],
    'Experience': [3, 7, 1, 5, 6]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display original dataset
print("Original DataFrame:\n")
print(df)

# Filter employees in the IT department with more than 5 years of experience
filtered_df = df[(df['Department'] == 'IT') & (df['Experience'] > 5)]

# Display filtered dataset
print("\nFiltered DataFrame:\n")
print(filtered_df)