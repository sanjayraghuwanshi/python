"""
Day 10 — Nested Dictionaries
Problem: Create a dictionary of 3 employees. Each employee has:

name, department, salary
Example:

employees = {
    "E001": {"name": "Anjali", "department": "HR", "salary": 55000},
    ...
}
1. Print each employee's full details.
2. Give everyone in "HR" a 10% salary raise and update their records.
3. Find the highest-paid employee.
4. List all unique departments.
Concepts: Nested dicts, updating nested values, sets for uniqueness
"""
from enum import unique

employees = {
    "E001": {"name": "Anjali", "department": "HR", "salary": 55000},
    "E002": {"name": "Shivani", "department": "Support", "salary": 50000},
    "E003": {"name": "Riya", "department": "Sales", "salary": 45000},
    "E004": {"name": "Bipasha", "department": "PS", "salary": 40000},
}
# 1
print(employees)

# 2
for employee in employees:
    if employees[employee]["department"] == "HR":
        employees[employee]["salary"] += (int(employees[employee]["salary"]) * 10) /100
print(employees)

# 3
highest_emp_id = max(employees, key=lambda x: employees[x]['salary'])
highest_emp = employees[highest_emp_id]
print(f"The highest paid employee is {highest_emp['name']} with a salary of {highest_emp['salary']}.")

# 4
uniq_dept = []

for employee in employees:
    dept = employees[employee]["department"]
    if dept not in uniq_dept:
        uniq_dept.append(dept)
print(uniq_dept)

#Other Method -
#uniq_dept = list({emp["department"] for emp in employees.values()})
#print(uniq_dept)