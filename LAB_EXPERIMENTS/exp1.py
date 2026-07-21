import numpy as np

student_scores = np.loadtxt(
    "data/Students_data.csv",
    delimiter=",",
    skiprows=1,
    usecols=(1, 2, 3, 4)
)

subjects = ["Math", "Science", "English", "History"]

average_scores = np.mean(student_scores, axis=0)

highest_subject = subjects[np.argmax(average_scores)]

print("Average Scores:")
for subject, avg in zip(subjects, average_scores):
    print(f"{subject}: {avg:.2f}")

print("\nHighest Average Subject:", highest_subject)