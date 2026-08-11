import pandas as pd
import matplotlib.pyplot as plt

# Read House Prices Dataset
df = pd.read_csv("data/house_sales.csv")

# Display basic information
print("========== HOUSE PRICE DATA ==========\n")
print(df["SalePrice"].describe())

# Plot Histogram
plt.figure(figsize=(8,5))
plt.hist(df["SalePrice"], bins=30, edgecolor="black", color="skyblue")

plt.title("Histogram of House Prices")
plt.xlabel("Sale Price")
plt.ylabel("Frequency")

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

# Check Skewness
skewness = df["SalePrice"].skew()

print("\nSkewness Value:", round(skewness, 2))

if skewness > 0:
    print("The data is Positively (Right) Skewed.")
elif skewness < 0:
    print("The data is Negatively (Left) Skewed.")
else:
    print("The data is Normally Distributed.")