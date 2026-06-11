"""
Day 20 — Functions as First-Class Objects
Problem:
========
1. Store three functions (add, subtract, multiply) in a list. Loop through and call each with (10, 5).
2. Write a function apply(func, value) that takes a function and a value, and applies the function to it.
3. Write a function make_multiplier(n) that returns a function that multiplies its input by n. Test: double = make_multiplier(2) then double(7) should give 14.
4. Use sorted() with a custom key function (not lambda) to sort a list of dictionaries by a field.
Concepts: Higher-order functions, closures, functions as arguments/return values
"""
from unittest import result


def add(*args):
    return sum(args)

def subtract(*args):
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result *= num
    return result

#print(add(10, 5))
#print(subtract(10, 5))
#print(multiply(10, 5))

operations = [add, subtract, multiply]
for func in operations:
    print(f"{func.__name__}: {func(10, 5)}")

def apply(func, value):
    return func(value)
# Usage examples:
# 1. Using a built-in function
print(apply(len, "Python"))  # Output: 6

def make_multiplier(n):
    # Inner function that uses 'n' from the outer scope
    def multiplier(x):
        return x * n
    return multiplier

# Testing the function
double = make_multiplier(2)
triple = make_multiplier(3)
print(f"{double.__name__}: {double(2)}")

print(double(7))  # Output: 14
print(triple(7))  # Output: 21

# Sample list of dictionaries
employees = [
    {"name": "Anjali", "salary": 55000},
    {"name": "Shivani", "salary": 50000},
    {"name": "Riya", "salary": 65000}
]

# 1. Define the custom key function
def get_salary(employee):
    return employee["salary"]

# 2. Use the function name as the 'key' argument
sorted_employees = sorted(employees, key=get_salary, reverse=True)  

# Output results
for emp in sorted_employees:
    print(emp)