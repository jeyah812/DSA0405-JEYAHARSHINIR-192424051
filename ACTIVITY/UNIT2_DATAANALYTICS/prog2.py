# ==========================================
# Fundamentals of Data Science
# Unit 2 - Data Preprocessing
# Experiment 2: Grouping
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

# Group by Department and calculate average marks
grouped_df = df.groupby('Department')['Marks'].mean()

# Display grouped data
print("\nAverage Marks by Department:\n")
print(grouped_df)