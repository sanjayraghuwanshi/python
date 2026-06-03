"""
Day 7 — Week 1 Mini Project: Student Grade Manager
Project: Build a console program that manages student grades.

Features:
Store student names and scores in a list (you can hardcode 8–10 students).
Display the full list sorted by score (highest first).
Show the top 3 students.
Show students who are below average.
Assign a grade: A (≥90), B (≥75), C (≥60), F (<60) and display it alongside each name.
Sample output:

=== Grade Report ===
1. Sneha    - 95 - A
2. Rahul    - 88 - B
3. Akshay    - 74 - C
...
Class Average: 76.4
Below Average: [Arjun (61), Dev (55)]
"""

# Central storage for student data
student_records = []

def add_student(name, marks):
    # Logic to determine grade based on marks
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # Store as a dictionary
    student = {
        "name": name,
        "marks": marks,
        "grade": grade
    }
    student_records.append(student)

# Store student names and scores in a list (you can hardcode 8–10 students).
add_student("Suniel", 92)
add_student("Akshay", 78)
add_student("Brion", 88)    
add_student("Brandon", 65)
add_student("Alex", 67)
add_student("Martin", 85)
add_student("Jim", 87)
add_student("Sanjay", 75)

# Display the full list sorted by score (highest first).
records = student_records
sorted_records = sorted(records, key=lambda x: x["marks"],reverse=True)
print(sorted_records)

# Show the top 3 students.
top_three = sorted_records[:3]
print(top_three)

# Show students who are below average.
below_average = [student['name'] for student in student_records if student['marks'] <= 70]
print(below_average)