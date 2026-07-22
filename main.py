import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read CSV File
df = pd.read_csv("D:\python\P3\marks.csv")

print("\n===== ORIGINAL DATA =====")
print(df)

# Select Marks Columns
marks = df[["Maths", "Science", "English"]]

# Total Marks
df["Total"] = marks.sum(axis=1)

# Percentage
df["Percentage"] = df["Total"] / 3

# Pass / Fail
df["Result"] = np.where(
    df["Percentage"] >= 35,
    "Pass",
    "Fail"
)

# Grade System
df["Grade"] = np.where(
    df["Percentage"] >= 90, "A+",
    np.where(
        df["Percentage"] >= 80, "A",
        np.where(
            df["Percentage"] >= 70, "B",
            np.where(
                df["Percentage"] >= 60, "C",
                "D"
            )
        )
    )
)

# Display Result Sheet
print("\n===== RESULT SHEET =====")
print(df)

# Topper
topper = df.loc[df["Percentage"].idxmax()]

print("\n===== TOPPER =====")
print(topper)

# Lowest Student
lowest = df.loc[df["Percentage"].idxmin()]

print("\n===== LOWEST STUDENT =====")
print(lowest)

# Pass Count
pass_count = (df["Result"] == "Pass").sum()

# Fail Count
fail_count = (df["Result"] == "Fail").sum()

print("\nPass Students :", pass_count)
print("Fail Students :", fail_count)

# Ranking
sorted_df = df.sort_values(
    by="Percentage",
    ascending=False
)

print("\n===== RANKING =====")
print(sorted_df)

# Subject Average
print("\n===== SUBJECT AVERAGE =====")
print(marks.mean())

# Subject Highest
print("\n===== SUBJECT HIGHEST =====")
print(marks.max())

# Subject Lowest
print("\n===== SUBJECT LOWEST =====")
print(marks.min())

# Students Above 80%
print("\n===== STUDENTS ABOVE 80% =====")
high_students = df[df["Percentage"] > 80]

print(high_students)

# Save Final Report
df.to_csv(
    "final_report.csv",
    index=False
)

print("\nReport Saved Successfully!")

# --------------------------
# BAR CHART
# --------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Name"],
    df["Percentage"]
)

plt.title("Student Percentage Analysis")
plt.xlabel("Student Name")
plt.ylabel("Percentage")

plt.show()

# --------------------------
# PIE CHART
# --------------------------

result_count = df["Result"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    result_count,
    labels=result_count.index,
    autopct="%1.1f%%"
)

plt.title("Pass vs Fail")

plt.show()