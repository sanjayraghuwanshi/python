fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# For loops with range function 

"""
for number in range(a, b):
    print(number)
"""
# Below loop with run between 1 to 10 where 10 is not included 
for number in range(1, 10):
    print(number)

# Below will step up the range by 3, so the output would be 1, 4, 7, 10
for number in range(1, 11, 3):
    print(number)

# Accumulate sum of 1..100 -> 5050
total = 0
for number in range(1, 101):
    total += number
print(total)