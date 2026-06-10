"""
Day 19 — Recursion
Problem:
========
Write a recursive function factorial(n) that computes n!
Write a recursive function fibonacci(n) that returns the nth Fibonacci number.
Write a recursive function sum_digits(n) that returns the sum of digits of a number. Example: sum_digits(1234) → 10
Write a recursive function flatten(nested_list) that flattens one level of nesting. Example: [[1,2],[3,4],[5]] → [1,2,3,4,5]
Concepts: Recursion, base case, call stack
"""
# 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
       return n * factorial(n-1)

print(factorial(5))

# 2
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(f"The 6th Fibonacci number is {fibonacci(7)}")

# 3
def sum_digits(n):
    s = str(abs(n))
    total_sum = 0
    if len(s) == 1:
        return int(s)
    for digit in s:
        total_sum += int(digit)
    return total_sum
#    using recursion
#    return int(s[0]) + sum_digits(int(s[1:]))
print(f"The sum of digits is {sum_digits(12345)}")

# 4
def flatten(nested_list):
    if not nested_list:
        return []

    return nested_list[0] + flatten(nested_list[1:])
my_list = [[1, 2], [3, 4], [5,6]]
print(flatten(my_list))