#1 year = 365 days, 52 weeks, 12 months
#Life span = 90 years
#https://waitbutwhy.com/2014/05/life-weeks.html

age = int(input("What is your current age?"))

total_days = 90 * 365
total_weeks = 90 * 52
total_months = 90 * 12

days_left = total_days - age * 365
weeks_left = total_weeks - age * 52
months_left = total_months - age * 12

print (f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")