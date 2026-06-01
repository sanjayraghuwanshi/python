"""
Problem: Given a list of 10 numbers (you choose them), do the following:

Print the first 4 numbers.
Print the last 3 numbers.
Print every alternate number.
Reverse the list without using .reverse().
Print the sorted version without modifying the original list.
Concepts: Slicing [start:end:step], sorted(), reversed()
"""

ran_num = [5,7,9,3,1,4,35,7,6,37]
print(f"Print the first 4 numbers : {ran_num[0:4]}")
print(f"Print the last 3 numbers : {ran_num[-3:]}")
print(f"Print the alternative numbers : {ran_num[0:len(ran_num):2]}")
print(f"reverse the list without using reverse() : {ran_num[::-1]}")
print(f"sort the list : {sorted(ran_num)}")