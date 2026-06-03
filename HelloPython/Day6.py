"""
Day 6 — List Methods & Sorting
Problem: You have a list of names: ["Zara", "Amit", "Priya", "John", "Meera", "Arjun"]

Sort alphabetically and print.
Sort by length of name (shortest first).
Sort by length, and for same-length names, sort alphabetically.
Find if "Priya" is in the list. Print her index.
Count how many names start with a vowel.
Concepts: sort() with key=, in, .index(), string methods
"""
names = ["Zara", "Amit", "Priya", "John", "Meera", "Arjun"]

# Sort alphabetically and print.
names.sort()
print(names)

# Sort by length of name (shortest first).
names.sort(key=len)
print(names)

# Sort by length, and for same-length names, sort alphabetically.
names.sort(key=lambda x: (len(x), x))
print(names)

# Find if "Priya" is in the list. Print her index.
print(names.index("Priya"))

# Count how many names start with a vowel.
count = sum(1 for name in names if name[0].lower() in 'aeiou')
print(count)