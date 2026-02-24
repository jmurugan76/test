import csv

# ===============================
# Step 1: Create Student Records
# ===============================

students = [
    ["Student Name", "Student Number", "Class", "Grade"],  # Header
    ["Arun Kumar", "S1001", "10A", "A"],
    ["Divya R", "S1002", "10B", "B+"],
    ["Karthik S", "S1003", "10A", "A-"],
    ["Meena Lakshmi", "S1004", "10C", "B"],
    ["Rahul Prasad", "S1005", "10B", "A+"]
]

# Write to CSV file
with open("student_records.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("Student records file created successfully.\n")

# ===============================
# Step 2: Read Student Records
# ===============================

print("Reading Student Records:\n")

with open("student_records.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
