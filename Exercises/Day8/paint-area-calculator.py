
"""
e.g. Height = 2, Width = 4, Coverage = 5
number of cans = (2 ✖️ 4) ÷ 5 = 1.6  #round up to 2
"""
import math

# match.ceil helps round the number to next whole number, 18.2 will be rounded to 19

def paint_area_calculate(height, width, cover):
    cans = math.ceil(height * width / cover)
    print(f"You'll need {cans} cans of paint.") 

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_area_calculate(height=test_h, width=test_w, cover=coverage)