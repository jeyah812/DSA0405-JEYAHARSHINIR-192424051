import pandas as pd

# Load customer dataset
df = pd.read_csv("data/customer_data.csv")

print("========== CUSTOMER DATASET ==========")
print(df)

# Create customer segments
def segment(spending):
    if spending >= 6000:
        return "High Spenders"
    elif spending >= 3000:
        return "Medium Spenders"
    else:
        return "Low Spenders"

df["Segment"] = df["Total Spending"].apply(segment)

# Display segmented customers
print("\n========== CUSTOMER SEGMENTS ==========")
print(df[["Customer ID", "Age", "Total Spending", "Segment"]])

# Calculate average age for each segment
average_age = df.groupby("Segment")["Age"].mean()

print("\n========== AVERAGE AGE BY SEGMENT ==========")
print(average_age.round(2))