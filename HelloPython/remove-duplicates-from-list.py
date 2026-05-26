numbers = [5,3,1,7,7,3,5,0,7,3,1,0,9,3,6,9]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print (uniques)