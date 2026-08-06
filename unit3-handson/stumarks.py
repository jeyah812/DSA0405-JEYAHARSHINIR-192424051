import pandas as pd

# Read Student Performance Dataset
df = pd.read_csv("data/StudentsPerformance.csv")

# Select Marks Column
marks = df["math score"]

# Calculate Quartiles
Q1 = marks.quantile(0.25)
Q3 = marks.quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate Limits
lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

# Detect Outliers
outliers = df[(marks < lower_limit) | (marks > upper_limit)]

print("========== STUDENT MARKS ==========\n")
print(marks)

print("\n========== IQR DETAILS ==========")
print("Q1 :", Q1)
print("Q3 :", Q3)
print("IQR :", IQR)
print("Lower Limit :", lower_limit)
print("Upper Limit :", upper_limit)

print("\n========== OUTLIERS ==========")

if outliers.empty:
    print("No outliers found.")
else:
    print(outliers[["math score"]])

print("\nTotal Outliers :", len(outliers))