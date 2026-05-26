'''
numbers = [5, 2, 5, 2, 2]
x="X"
for num in numbers:
    print(x * num)
'''

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for  count in range(x_count) :
        output += 'x'
    print(output)

x=''
print('='*10)

numbers = [2, 2, 2, 2, 8]
for x_count in numbers:
    output = ''
    for  count in range(x_count) :
        output += 'x'
    print(output)