import pandas as pd
from collections import Counter
import string

# Read Dataset
df = pd.read_csv("data/customer_reviews.csv")

# Combine all reviews
text = " ".join(df["Review"]).lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Split into words
words = text.split()

# Count frequency
frequency = Counter(words)

print("========== WORD FREQUENCY ==========\n")

for word, count in frequency.items():
    print(word, ":", count)