"""
Small Pizza: $15 | Medium Pizza: $20 | Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
Example output - Your final bill is: $28.
"""
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

Small_Pizza = 15
Medium_Pizza = 20
Large_Pizza = 25

if size == "S":
    if add_pepperoni == "Y":
        Small_Pizza += 2
    if extra_cheese == "Y":
        Small_Pizza += 1
        print(f"Your final bill is: ${Small_Pizza}")
    else: 
        print(f"Your final bill is: ${Small_Pizza}")

if size == "M":
    if add_pepperoni == "Y":
        Medium_Pizza += 3
    if extra_cheese == "Y":
        Medium_Pizza += 1
        print(f"Your final bill is: ${Medium_Pizza}")
    else: 
        print(f"Your final bill is: ${Medium_Pizza}")

if size == "L":
    if add_pepperoni == "Y":
        Large_Pizza += 3
    if extra_cheese == "Y":
        Large_Pizza += 1
        print(f"Your final bill is: ${Large_Pizza}")
    else: 
        print(f"Your final bill is: ${Large_Pizza}")

"""
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")
"""