import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import string

# Read Dataset
df = pd.read_csv("data/data.csv")

# Combine all feedback
text = " ".join(df["feedback"]).lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Stop words
stop_words = {
    "the","is","and","to","a","an","of",
    "with","very","in","for","on"
}

# Remove stop words
words = [word for word in text.split() if word not in stop_words]

# Frequency Distribution
frequency = Counter(words)

# User Input
n = int(input("Enter Top N Words: "))

top_words = frequency.most_common(n)

print("\nTop", n, "Most Frequent Words:\n")

for word, count in top_words:
    print(word, ":", count)

# Plot Bar Chart
labels = [item[0] for item in top_words]
counts = [item[1] for item in top_words]

plt.figure(figsize=(8,5))
plt.bar(labels, counts, color="skyblue", edgecolor="black")

plt.title("Top Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()