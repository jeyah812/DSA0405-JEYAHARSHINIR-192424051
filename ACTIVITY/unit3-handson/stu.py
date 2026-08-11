import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("data/StudentsPerformance.csv")

# Create Grade column from Math Score
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["math score"].apply(get_grade)

# Frequency Distribution
grade_frequency = df["Grade"].value_counts().sort_index()

print("========== GRADE FREQUENCY DISTRIBUTION ==========\n")
print(grade_frequency)

# Bar Chart
plt.figure(figsize=(6,4))
plt.bar(grade_frequency.index, grade_frequency.values,
        color="skyblue", edgecolor="black")

plt.title("Frequency Distribution of Students' Grades")
plt.xlabel("Grade")
plt.ylabel("Number of Students")

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()