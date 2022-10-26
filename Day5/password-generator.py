import random
import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#For letters
p_letters = ""
for i in range(0, nr_letters):
    randomLetter = random.choice(letters)
    p_letters = f'{p_letters}{randomLetter}'
#print(p_letters)

#For numbers
p_number = ""
for i in range(0, nr_numbers):
    random_integer = random.randint(0, 9)
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

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

n_pass = p_letters + p_symbol + p_number

l = list(n_pass)
len = len(n_pass)
print(l)

p_random = random.shuffle(l)
print(f"Here is your Hard password: {p_random}")

#res = p_number + p_symbol + p_letters