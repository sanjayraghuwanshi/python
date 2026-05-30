#numbers = [1,2,3,4,5,6,7,8,9]

def find_max(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = numbers[i]
    return max

numbers = [10,4,7,2,9,0]
max = find_max(numbers)
#print(max(1,2,3,4,5))
print(max)