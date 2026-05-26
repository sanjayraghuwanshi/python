weight = input('Weight: ')
unit = (input(f"(L)bs or (K)g: "))
if unit.lower() == "k":
    print("You are ", (int(weight) * 2.20) , "Pounds")
else :
    print("You are ", round((int(weight) * 0.45)) , "Kgs")