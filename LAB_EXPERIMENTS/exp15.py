import pandas as pd

# Read CSV
df = pd.read_csv("data/likes.csv")

# Frequency Distribution
frequency = df["Likes"].value_counts().sort_index()

print("Frequency Distribution of Likes:\n")
print(frequency)