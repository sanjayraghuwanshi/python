"""
print - Welcome to the tip calculator
input - What as the total bill?
input - What percentage tip would you like to give? 10, 12, or 15?
input - How many people to split the bill ?
print - Each person should pay: 
"""

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_pct = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = float(input("How many people to split the bill? "))

one_percent = round(bill / 100, 2) 
total_bill = bill + one_percent * tip_pct
final_amount = round(total_bill / split,2)
bill_per_person = "{:.2f}".format(final_amount) 
print(f"Each person should pay: ${bill_per_person}")