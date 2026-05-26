'''
names = ['Tom', 'Dick', 'Harry', 'Darry']
print(names[0])
print(names[-1])
print(names[1:4])
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest_number = numbers[0]
for i in numbers:
    if i > largest_number:
        largest_number = i
print(largest_number)