"""
Day 15 — Function Basics & Return Values
Problem: Write the following functions:

greet(name) — returns "Hello, <name>!"
celsius_to_fahrenheit(c) — converts and returns the value.
is_palindrome(word) — returns True if the word reads the same forwards and backwards.
count_vowels(text) — returns the number of vowels in a string.
Test each function with at least 2 inputs and print results.
Concepts: def, return, calling functions
"""
def greet(name):
    print(f"Hello, {name}!")

def celsius_to_fahrenheit(c):
    fahrenheit = (c * 9 / 5) + 32
    return fahrenheit

def is_palindrome(word):
    return word.lower() == word[::-1]

def count_vowels(text):
    count = 0
    for letter in text:
        if letter.lower() == 'a' or letter == 'e' or letter == 'i' or letter == 'u':
            count += 1
    return count

greet("Sanjay Raghuwanshi")

f = celsius_to_fahrenheit(40)
print(f"Celsius to Fahrenheit : {f}")

p = is_palindrome("level")
print(f"This is palindrome (True/False) : {p}")

c = count_vowels("SALSA")
print(f"Count of vowels for this word is : {c}")