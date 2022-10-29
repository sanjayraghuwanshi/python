"""
It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.

BMI = weight/height ** 2
bmi_as_int = int(BMI)
print(bmi_as_int)
"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = weight/height ** 2
bmi_as_int = round(BMI)

## Better way of rounding - BMI = round(weight/height ** 2)

if BMI < 18.5:
    print(f"Your BMI is {bmi_as_int}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {bmi_as_int}, you are slightly overweight.") 
elif BMI < 35:
    print(f"Your BMI is {bmi_as_int}, you are obese.") 
else:
    print(f"Your BMI is {bmi_as_int}, you are clinically obese.")