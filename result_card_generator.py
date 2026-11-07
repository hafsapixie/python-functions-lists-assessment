
# Student Result Card Generator

print("===== Student Result Card Generator =====")

# Function 1: Format student name
def format_name(name):
    return name.strip().title()


# Function 2: Validate and get subject marks
def get_valid_marks(subject):
    while True:
        marks = input(f"Enter marks for {subject} (0-100): ")

        if marks.isdigit():
            marks = int(marks)

            if marks >= 0 and marks <= 100:
                return marks

            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        else:
            print("Invalid input! Please enter numbers only.")


# Function 3: Calculate percentage
def calculate_percentage(total, max_total):
    return (total / max_total) * 100


# Function 4: Get grade
def get_grade(percentage):
    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "Fail"


# Step 1: Collect student information
name = format_name(input("Enter student name: "))

# Validate roll number
while True:
    roll_number = input("Enter roll number: ")

    if roll_number.isdigit():
        break

    else:
        print("Invalid roll number! Enter digits only.")


# Step 2: Collect marks for five subjects
subjects = ["English", "Mathematics", "Computer", "Physics", "Chemistry"]

total_marks = 0
failed_subject = False

for subject in subjects:

    marks = get_valid_marks(subject)

    total_marks = total_marks + marks

    if marks < 40:
        failed_subject = True


# Step 3: Calculate percentage and grade
max_total = 500

percentage = calculate_percentage(total_marks, max_total)

grade = get_grade(percentage)


# Step 4: Check final result
if failed_subject:
    result = "Fail"
    grade = "Fail"

else:
    result = "Pass"


# Step 5: Display result card
print("\n======================================")
print("           STUDENT RESULT CARD")
print("======================================")

print(f"Student Name : {name}")
print(f"Roll Number  : {roll_number}")

print("--------------------------------------")
print(f"Total Marks  : {total_marks}/{max_total}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")
print(f"Result       : {result}")

print("======================================")
