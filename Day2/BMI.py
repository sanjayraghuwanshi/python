"""
enter your height
enter your weight
1 meter = 3.28084 foot
BMI = weight/height ** 2 (in meters)
"""
height = float(input("enter your height in meters:"))
weight = float(input("enter your weight in kgs:"))
BMI = weight/height ** 2
bmi_as_int = int(BMI)
print(bmi_as_int)

"""
another way of doing it 
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

h = float(height)
w = float(weight)
BMI = str(w/h ** 2)
print(str(BMI[:2]))
"""