
def greet():
    print("Hello")
    print("Good Morning Sanjay")

greet()

# name here is the parameter 
# value to name while calling function is called argument

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Good Morning {name}")

greet_with_name("Sanjay")   # Sanjay here is the argument for function greet_with_name

greet_with_name("Billie")

#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Good Morning from {location}")

greet_with("Sanjay", "Bangalore")
# OR 
greet_with(location="Bangalore",name="Sanjay")