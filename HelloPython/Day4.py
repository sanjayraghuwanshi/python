"""
Day 4 — List Comprehensions
Problem: Rewrite the following using list comprehensions (one line each):

A list of squares of numbers from 1 to 10.
A list of only even numbers from 1 to 20.
A list of words from ["apple", "banana", "cherry", "date", "elderberry"] that have more than 5 characters.
A list of uppercase versions of the above filtered words.
Concepts: List comprehensions, filtering with conditions
"""
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# List comprehension to square numbers from 1 to 10
print(f"Squares = {[x**2 for x in range(1, 11)]}")
print(f"Even numbers = {[x for x in range(2, 21,2)]}")
print(f"Fruit with more than 5 char = {[x for x in fruits if len(x) > 5]}")
print(f"Fruits list in upper case = {[x.upper() for x in fruits if len(x) > 5]}")