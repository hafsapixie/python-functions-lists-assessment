# Python Functions & Lists Assessment

A beginner-friendly Python project demonstrating functions, string manipulation, lists, and loops through two practical applications.

## Repository Information

**Repository Name:** `python-functions-lists-assessment`

**Programming Language:** Python 3

## Project Overview

This project contains two Python applications developed as part of the Functions & Lists Assessment.

### Task 1: Student Result Card Generator

**File:** `result_card_generator.py`

A Python application that generates a student's result card based on their marks in five subjects.

**Features:**

- Collects student name, roll number, and marks in five subjects.
- Formats student names using `.strip()` and `.title()`.
- Validates roll numbers using `.isdigit()`.
- Validates subject marks between 0 and 100.
- Calculates total marks and percentage.
- Assigns grades according to the percentage.
- Checks individual subject passing criteria.
- Displays a formatted result card using f-strings.

**Grading Criteria:**

| Percentage | Grade |
|---|---|
| 90% and above | A+ |
| 80% – 89% | A |
| 70% – 79% | B |
| 60% – 69% | C |
| 50% – 59% | D |
| Below 50% | Fail |

**Passing Criteria:** A student must score at least 40 marks in every subject to pass. If any subject has marks below 40, the final result is Fail regardless of the overall percentage.

### Task 2: Class Marks Analyzer

**File:** `class_marks_analyzer.py`

A Python application that analyzes the academic performance of an entire class.

**Features:**

- Collects the number of students, names, and marks.
- Stores student names and marks in separate lists.
- Validates marks between 0 and 100.
- Calculates the class average.
- Identifies students with the highest and lowest marks.
- Counts passing and failing students.
- Displays students who scored above the class average.
- Sorts students from highest to lowest marks.
- Generates a complete class performance report.

**Passing Criteria:**

- Passing marks: 50 or above.
- Failing marks: Below 50.

## Python Concepts Covered

The following Python concepts are demonstrated in this project:

**Functions and Strings:**

- Function definition using `def`.
- Parameters and arguments.
- `return` statement.
- String methods: `.strip()`, `.title()`, `.isdigit()`.
- f-strings.
- Input validation.

**Lists and Loops:**

- Creating empty lists.
- Adding elements using `.append()`.
- Finding list length using `len()`.
- Calculating totals using `sum()`.
- Finding highest and lowest values using `max()` and `min()`.
- Sorting using `sorted()`.
- Combining lists using `zip()`.
- `for` and `while` loops.
- Conditional statements (`if`, `elif`, `else`).
- Counters and accumulators.

## Project Structure

```text
python-functions-lists-assessment/
│
├── result_card_generator.py
├── class_marks_analyzer.py
└── README.md
```

## Requirements

- Python 3.x
- Visual Studio Code or any Python-supported code editor.

## Sample Input/Output

### Task 1: Student Result Card Generator

**Sample Input:**

```text
Enter student name: ali ahmed
Enter roll number: 1025

Enter marks for English (0-100): 85
Enter marks for Mathematics (0-100): 90
Enter marks for Computer (0-100): 95
Enter marks for Physics (0-100): 80
Enter marks for Chemistry (0-100): 88
```

**Sample Output:**

```text
======================================
           STUDENT RESULT CARD
======================================
Student Name : Ali Ahmed
Roll Number  : 1025
--------------------------------------
Total Marks  : 438/500
Percentage   : 87.60%
Grade        : A
Result       : Pass
======================================
```

### Task 2: Class Marks Analyzer

**Sample Input:**

```text
How many students are in the class? 3

Enter name of student 1: Has
Enter marks for Has (0-100): 55

Enter name of student 2: Gmgm
Enter marks for Gmgm (0-100): 56

Enter name of student 3: Bnvb
Enter marks for Bnvb (0-100): 77
```

**Sample Output:**

```text
=================================================
              CLASS MARKS ANALYZER REPORT
=================================================
Total students       : 3
Class average        : 62.67
Highest marks        : 77
Highest scorer(s)    : Bnvb
Lowest marks         : 55
Lowest scorer(s)     : Has
Passing students     : 3
Failing students     : 0
-------------------------------------------------
Students who scored above the class average:
    Bnvb: 77
-------------------------------------------------
Students sorted by marks (highest to lowest):
    1. Bnvb: 77
    2. Gmgm: 56
    3. Has: 55
=================================================
```

## Author
**Hafsa Naseer**
Created as part of the Python Functions & Lists Assessment.