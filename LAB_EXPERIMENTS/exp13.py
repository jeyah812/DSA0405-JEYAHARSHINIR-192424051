from collections import Counter

# Read text file
with open("data/sample_text.txt", "r") as file:
    text = file.read().lower()

# Remove punctuation
text = text.replace(".", "").replace(",", "")

# Split into words
words = text.split()

# Count frequency
frequency = Counter(words)

print("Word Frequency Distribution:\n")

for word, count in frequency.items():
    print(word, ":", count)