"""
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.
"""
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lc = name1.lower()
name2_lc = name2.lower()

name = name1_lc + name2_lc

T_n1 = name.count('t')
R_n1 = name.count('r')
U_n1 = name.count('u')
E_n1 = name.count('e')
L_n2 = name.count('l')
O_n2 = name.count('o')
V_n2 = name.count('v')
E_n2 = name.count('e')

sum_name1 = T_n1 + R_n1 + U_n1 + E_n1
sum_name2 = L_n2 + O_n2 + V_n2 + E_n2

sum_name = int(str(sum_name1) + str(sum_name2))

if sum_name < 10 or sum_name > 90:
    print(f"You score is {sum_name}, you go together like coke and mentos.")

elif sum_name < 50 and sum_name > 40:
    print(f"Your score is {sum_name}, you are alright together.")
else:
    print(f"Your score is {sum_name}.")