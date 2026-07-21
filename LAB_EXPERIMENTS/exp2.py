import pandas as pd

# Read the CSV file
df = pd.read_csv("data/Sales_data.csv")

# Find average price for November 2023
average_price = df[df["Month_sales"] == "November 2023"]["Price"].mean()

print("Average Price in November 2023:", average_price)