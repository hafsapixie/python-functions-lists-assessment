
# Class Marks Analyzer

print("=" * 65)
print("                    CLASS MARKS ANALYZER")
print("=" * 65)

# Step 1: Ask number of students
total_students = int(input("How many students are in the class? "))

# Step 2: Create two empty lists
student_names = []
student_marks = []

# Step 3: Collect student information
for i in range(total_students):

    name = input(f"Enter name of student {i + 1}: ")

    while True:
        marks = input(f"Enter marks for {name} (0-100): ")

        if marks.isdigit():
            marks = int(marks)

            if marks >= 0 and marks <= 100:
                break
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        else:
            print("Invalid input! Enter numbers only.")

    student_names.append(name)
    student_marks.append(marks)


# Step 4: Calculate class average
class_average = sum(student_marks) / len(student_marks)

# Step 5: Find highest and lowest marks
highest_marks = max(student_marks)
lowest_marks = min(student_marks)


# Step 6: Count passing and failing students
passing_count = 0
failing_count = 0

for marks in student_marks:

    if marks >= 50:
        passing_count = passing_count + 1

    else:
        failing_count = failing_count + 1


# Step 7: Display class report
print("\n" + "=" * 65)
print("                 CLASS MARKS ANALYZER REPORT")
print("=" * 65)

print(f"Total students       : {total_students}")
print(f"Class average        : {class_average:.2f}")
print(f"Highest marks        : {highest_marks}")

# Display highest scorer(s)
for i in range(len(student_marks)):

    if student_marks[i] == highest_marks:
        print(f"Highest scorer(s)    : {student_names[i]}")

# Display lowest scorer(s)
for i in range(len(student_marks)):

    if student_marks[i] == lowest_marks:
        print(f"Lowest scorer(s)     : {student_names[i]}")

print(f"Passing students     : {passing_count}")
print(f"Failing students     : {failing_count}")

print("-" * 65)

# Step 8: Display students above class average
print("Students who scored above the class average:")

for i in range(len(student_marks)):

    if student_marks[i] > class_average:
        print(f"    {student_names[i]}: {student_marks[i]}")

print("-" * 65)


# Step 9: Sort students & marks from highest to lowest

sorted_students = sorted(zip(student_marks, student_names), reverse=True)

print("Students sorted by marks (highest to lowest):")

for i in range(len(sorted_students)):
    print(f"    {i + 1}. {sorted_students[i][1]}: {sorted_students[i][0]}")

print("=" * 65)
