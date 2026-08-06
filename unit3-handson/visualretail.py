import pandas as pd
import matplotlib.pyplot as plt

# Read Superstore Dataset
df = pd.read_csv("data/Superstore.csv", encoding="latin1")

# Sales Column
sales = df["Sales"]

# Calculate IQR
Q1 = sales.quantile(0.25)
Q3 = sales.quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

# Remove Outliers
cleaned_df = df[(sales >= lower_limit) & (sales <= upper_limit)]

# -------------------------
# Histogram Before
# -------------------------
plt.figure(figsize=(6,4))
plt.hist(df["Sales"], bins=30, edgecolor="black")
plt.title("Histogram Before Removing Outliers")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# -------------------------
# Box Plot Before
# -------------------------
plt.figure(figsize=(4,5))
plt.boxplot(df["Sales"])
plt.title("Box Plot Before Removing Outliers")
plt.ylabel("Sales")
plt.show()

# -------------------------
# Histogram After
# -------------------------
plt.figure(figsize=(6,4))
plt.hist(cleaned_df["Sales"], bins=30, edgecolor="black")
plt.title("Histogram After Removing Outliers")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# -------------------------
# Box Plot After
# -------------------------
plt.figure(figsize=(4,5))
plt.boxplot(cleaned_df["Sales"])
plt.title("Box Plot After Removing Outliers")
plt.ylabel("Sales")
plt.show()

print("Original Records :", len(df))
print("Records After Removing Outliers :", len(cleaned_df))