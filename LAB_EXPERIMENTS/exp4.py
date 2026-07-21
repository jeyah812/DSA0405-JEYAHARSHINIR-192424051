import numpy as np

sales_data = np.genfromtxt(
    "data/Sales_data1.csv",
    delimiter=",",
    skip_header=1,
    dtype=str
)

months = sales_data[:, 1]
sales = sales_data[:, 4].astype(float)

q4_months = ["October", "November", "December"]

q4_sales = sales[np.isin(months, q4_months)]

average_sales = np.mean(q4_sales)

print("Average Sales in Q4:", average_sales)