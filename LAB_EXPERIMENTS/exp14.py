import pandas as pd

# Read CSV
df = pd.read_csv("data/customers.csv")

# Frequency Distribution
frequency = df["Age"].value_counts().sort_index()

print("Frequency Distribution of Customer Ages:\n")
print(frequency)