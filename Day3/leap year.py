""" 
A year is a leap year if the following conditions are satisfied: 
The year is multiple of 400.
The year is multiple of 4 and not multiple of 100.
"""

year = int(input("Which year do you want to check? "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("This year is a leap year")
else:
    print("This year is not a leap year")


"""
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
"""