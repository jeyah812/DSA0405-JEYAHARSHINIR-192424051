# ==========================================
# Fundamentals of Data Science
# Unit 2 - Data Preprocessing
# Experiment 5: Using head() and tail()
# ==========================================

import pandas as pd

# Creating a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'Score': [85, 92, 78, 95, 88, 72, 91]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display original dataset
print("Original DataFrame:\n")
print(df)

# Display the first 5 rows (default)
print("\nFirst 5 Rows:")
print(df.head())

# Display the first 2 rows
print("\nFirst 2 Rows:")
print(df.head(2))

# Display the last 3 rows
print("\nLast 3 Rows:")
print(df.tail(3))