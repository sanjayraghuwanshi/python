"""
Day 17 — *args and **kwargs
Problem:
========
1. Write add_all(*numbers) that accepts any number of arguments and returns their sum.
2. Write print_profile(**details) that prints each key-value pair nicely.
Example call: print_profile(name="Meera", city="Pune", hobby="Painting")
3. Write summarize(*words, **counts) that prints the list of words and their counts dictionary.
4. Call a function using *list_var and **dict_var to unpack them as arguments.
Concepts: *args, **kwargs, unpacking
"""

# 1
def add_all(*numbers):
    return sum(numbers)

sum = add_all(1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(f" Sum of all the numbers : {sum}")

# 2
def print_profile(**details):
    print(details)

print_profile(Name="Meera", City="Pune", Hobby="Painting")

# 3
def summarize(*words, **counts):
    print("Words List:" , list(words))
    print("Counts Dictionary:" , counts)

summarize("apple", "banana", "cherry", apple=5, banana=2, cherry=10)
summarize("apple", "banana", "cherry")

# 4
def display_profile(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Call the function by unpacking both
display_profile("Amit", 30, "Pune")

# Data stored in collections
list_var = ["Arjun", 28]
dict_var = {"city": "Mumbai"}
display_profile(*list_var, **dict_var)
