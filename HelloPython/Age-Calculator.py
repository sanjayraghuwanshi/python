birth_year = input(f"Enter your birth year: ")
# input is always taking sting as input
age = 2026 - int(birth_year)
#print(age, 'years old')
'''
if you want to add string at the beginning then concat won't work without converting age into string.
'''
print(f"You are, {age} years old")