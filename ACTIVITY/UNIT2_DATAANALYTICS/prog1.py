# ==========================================
# Fundamentals of Data Science
# Unit 2 - Data Preprocessing
# Experiment 1: Sorting
# ==========================================

import pandas as pd

# Creating a sample dataset
data = {
    'Name': ['Arun', 'Bala', 'Chitra', 'Divya', 'Ezhil', 'Fathima'],
    'Department': ['CSE', 'ECE', 'CSE', 'ECE', 'CSE', 'ECE'],
    'Marks': [85, 78, 92, 88, 75, 95]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display original dataset
print("Original Data:\n")
print(df)

# Sort data by Marks in descending order
sorted_df = df.sort_values(by='Marks', ascending=False)

# Display sorted data
print("\nSorted Data (Highest to Lowest Marks):\n")
print(sorted_df)