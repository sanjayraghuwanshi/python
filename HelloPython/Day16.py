"""
Day 16 — Default & Keyword Arguments
Problem:
=======
1. Write make_greeting(name, greeting="Hello", punctuation="!") that returns a customized greeting.
Test with: just a name, name + greeting, all three args.
2. Write power(base, exponent=2) that returns base raised to exponent. Default is squaring.
3. Write describe_person(name, age, city="Unknown") — test calling it with and without city.
4. What happens when you call make_greeting(greeting="Hi", name="Ravi")? Try it and explain in a comment.
Concepts: Default args, keyword args, argument order
"""
from email.policy import default

# 1
def make_greeting(greeting="Hello", name="", punctuation="!"):
    name = name
    greeting = greeting
    punctuation = punctuation
    print(f"{greeting} {name} {punctuation}")

make_greeting(greeting="Hi" ,name="Pritam", punctuation="!!")
make_greeting(name="Raghav")
make_greeting(greeting="Helloww")

# 2
def power(base, exponent=2):
    return base ** exponent

print(power(base=4, exponent=2))
print(power(5,4))
print(power(5))

# 3
def describe_person(name, age, city="Unknown"):
    return f"Name : {name} \n Age : ({age}) \n City : {city}"
print(describe_person(name="Pritam", age=40, city="Pune"))
print(describe_person(name="Pritam", age=40))

# 4
make_greeting(greeting="Hi", name="Ravi")