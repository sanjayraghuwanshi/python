import random 

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

#print(random.random())

random_number = random.random()
random_integer = int(random_number)

if random_integer % 2 == 0:
    print("Heads")
else:
    print("Tails")

"""
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
"""