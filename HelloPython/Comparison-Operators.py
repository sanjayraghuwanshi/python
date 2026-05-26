# x = 20 - here equals sign is assigment operator.
# x ==20 - here == is comparison operator.

temp = input("Whats the temperature today?")
if int(temp) > 30 :
    print("Its a hot day")
elif int(temp) < 10:
    print("Its a cold day")
else :
    print("Its neither hot nor cold")