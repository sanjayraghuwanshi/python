import random
import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#EASY ONE 
#########
"""
#For letters
p_letters = ""
for i in range(0, nr_letters):
    randomLetter = random.choice(letters)
    p_letters = f'{p_letters}{randomLetter}'

#Other way of doing above is 
#for i in range(0, nr_letters):
#    p_letters += random.choice(letters)

#For numbers
p_number = ""
for i in range(0, nr_numbers):
    random_integer = random.choice(numbers)
    p_number = f'{p_number}{random_integer}'
#print(p_number)

# for symbols
p_symbol = ""
for i in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    p_symbol = f'{p_symbol}{random_symbol}'
#print(p_symbol)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print(f"Here is your easy password: {p_letters}{p_symbol}{p_number}")

"""

#HARD_ONE

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for i in range(0, nr_letters):
    password_list += random.choice(letters)     # OR password_list.append(random.choice(letters))

for i in range(0, nr_numbers):
    password_list += random.choice(numbers)

for i in range(0, nr_symbols):
    password_list += random.choice(symbols)

#print(password_list)
new_p = random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Here is your hard password: {new_p}")