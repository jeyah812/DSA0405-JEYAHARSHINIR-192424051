import pandas as pd

# Load sales dataset
df = pd.read_csv("data/sales_data5.csv")

print("========== SALES DATASET ==========")
print(df)

# Calculate Total Sales
df["Total Sales"] = df["Quantity Sold"] * df["Unit Price"]

# Calculate Profit with 20% margin
df["Profit"] = df["Total Sales"] * 0.20

# Total sales for each product
product_sales = df.groupby("Product")["Total Sales"].sum()

# Total profit for each product
product_profit = df.groupby("Product")["Profit"].sum()

# Overall profit
overall_profit = df["Profit"].sum()

print("\n========== TOTAL SALES BY PRODUCT ==========")
print(product_sales)

print("\nOverall Sales: ₹", round(df["Total Sales"].sum(), 2))

print("\nOverall Profit: ₹", round(overall_profit, 2))

# Top 5 profitable products
top_products = product_profit.sort_values(ascending=False).head(5)

print("\n========== TOP 5 MOST PROFITABLE PRODUCTS ==========")
print(top_products)