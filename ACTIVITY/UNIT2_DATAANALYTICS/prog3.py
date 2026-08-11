# ==========================================
# Fundamentals of Data Science
# Unit 2 - Data Preprocessing
# Experiment 3: Ranking
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

# Assign ranks based on marks (Highest marks get Rank 1)
df['Rank'] = df['Marks'].rank(ascending=False, method='dense')

# Display ranked data
print("\nStudents with Rank:\n")
print(df.sort_values(by='Rank'))