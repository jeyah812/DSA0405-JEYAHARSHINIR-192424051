# ==========================================
# Fundamentals of Data Science
# Unit 2 - Data Preprocessing
# Experiment 4: Plotting
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

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

# Plot a bar chart of student marks
plt.figure(figsize=(8, 5))

plt.bar(df['Name'], df['Marks'])

plt.title("Student Marks")

plt.xlabel("Student Name")

plt.ylabel("Marks")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

grouped_df = df.groupby('Department')['Marks'].mean()

grouped_df.plot(kind='bar')

plt.title("Average Marks by Department")

plt.xlabel("Department")

plt.ylabel("Average Marks")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()