import csv
import os

file_name = "student_records.csv"

# ==============================
# 1️⃣ WRITE OPERATION (Create File)
# ==============================

students = [
    ["Student Name", "Student Number", "Class", "Grade"],  # Header
    ["Arun Kumar", "S1001", "10A", "A"],
    ["Divya R", "S1002", "10B", "B+"],
    ["Karthik S", "S1003", "10A", "A-"],
    ["Meena Lakshmi", "S1004", "10C", "B"],
    ["Rahul Prasad", "S1005", "10B", "A+"]
]

with open(file_name, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("✅ 5 Student records written successfully.\n")


# ==============================
# 2️⃣ READ OPERATION
# ==============================

print("📖 Reading Student Records:\n")

with open(file_name, mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("\n")


# ==============================
# 3️⃣ APPEND OPERATION
# ==============================

new_student = ["Sneha Iyer", "S1006", "10A", "A"]

with open(file_name, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_student)

print("➕ New student record appended successfully.\n")


# ==============================
# 4️⃣ READ AGAIN (After Append)
# ==============================

print("📖 Updated Student Records:\n")

with open(file_name, mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
