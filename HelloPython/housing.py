price_house = 1000000
credit_score = input('What is your credit score')
good_credit = False
if int(credit_score) >= 850:
    print('You need to put down 10% down payment')
    down_payment = price_house * 10 / 100
    print(f'Your down payment will be $ {down_payment}')
else:
    print('You need to put down 20% down payment')
    down_payment = price_house * 20  / 100
    print(f'Your down payment will be $ {down_payment}')
