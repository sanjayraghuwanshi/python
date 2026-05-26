numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(f'Append 20 at the end:\t {numbers}')
numbers.insert(0, 10)
print(f"Inset 10 at the index '0':\t {numbers}")
numbers.remove(2)
print(f"Remove the number 2 from the list:\t {numbers}")
numbers.pop()   # removes last item from the list.
print(f"Pop out the last entry:\t {numbers}")
#numbers.clear()    #clear content of list.
print(f"Print index of 5:\t {numbers.index(5)}") # print index of 5 from the list
print(f"Check if 50 exists:\t {50 in numbers}") # to check if exists in boolean
print(f"Print count of 5:\t {numbers.count(5)}")
numbers.sort()
print(f"Sort the list:\t {numbers}")