#Day4

import random

# it'll print a random int number between 1 to 10 each time program is executed.
random_integer = random.randint(1, 10)
print(random_integer)

# it'll print a random float number between 0 to 1 each time program is executed.
random_float = random.random()
print(random_float)

# it'll print a random float number between 0.0 to 5.0 each time program is executed.
random_float1 = random_float * 5
print(random_float1)

# Other way of doing above is to multiple random_float with 5 each time
random_float = random.uniform(0.0, 5.0)
print(random_float)
