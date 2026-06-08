"""
Day 18 — Scope & Lambda Functions
Problem:
========
1. Demonstrate the difference between a local and global variable with a short example.
2. Use the global keyword to modify a global variable inside a function. Show before and after.
3. Write a lambda to: square a number, check if a number is even, convert a name to uppercase.
4. Use map() with a lambda to square all numbers in [1, 2, 3, 4, 5].
5. Use filter() with a lambda to keep only even numbers from [1, 2, 3, 4, 5, 6, 7, 8].
Concepts: Scope, global, lambda, map(), filter()
"""
# 1 & 2
# before
name = "Sanjay"
def greet():
    print(name)
greet()

# After
def greet():
    global name
    name = "Raghuwanshi"
    print(name)
greet()

# Square a number
square = lambda x: x ** 2
print(square(5))

# Check if number is even
is_even = lambda x: x % 2 == 0
print(is_even(8))

# Convert a name to an uppercase
to_upper = lambda name: name.upper()
print(to_upper("raghuwanshi"))

# Use map with lambda to square each number
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# Use filter() with a lambda to keep only even numbers from [1, 2, 3, 4, 5, 6, 7, 8].
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)