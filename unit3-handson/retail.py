import pandas as pd

# Read Superstore Dataset
df = pd.read_csv("data/Superstore.csv", encoding="latin1")

print("========== SALES DATA ==========\n")
print(df[["Sales"]].head())

# Calculate Quartiles
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate Lower and Upper Limits
lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

# Remove Outliers
cleaned_df = df[(df["Sales"] >= lower_limit) &
                (df["Sales"] <= upper_limit)]

print("\n========== IQR DETAILS ==========")
print("Q1 :", Q1)
print("Q3 :", Q3)
print("IQR :", IQR)
print("Lower Limit :", lower_limit)
print("Upper Limit :", upper_limit)

print("\nOriginal Records :", len(df))
print("Records After Removing Outliers :", len(cleaned_df))

print("\n========== CLEANED DATASET ==========")
print(cleaned_df.head())

# Save Cleaned Dataset
cleaned_df.to_csv("Cleaned_Sales.csv", index=False)

print("\nCleaned dataset saved as 'Cleaned_Sales.csv'")