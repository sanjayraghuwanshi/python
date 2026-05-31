import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_integer = random.randint(0, len(names) - 1)
#print(random_integer)
payer = names[random_integer]
#print(payer)
print(f"{payer} is going to buy the meal today!")

#Other way of doing it, instead of line 9-11 - 
#payer = random.choice(names)
#print(f"{payer} is going to buy the meal today!")