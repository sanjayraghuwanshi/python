def greet_user(first_name, last_name):
    print(f'Hi, {first_name}, {last_name}')
    print('Welcome Aboard')
...

print("Start")
greet_user("John", "Doe")
#keyword arguments is when you define the keys
greet_user(last_name="John", first_name="Doe")
print("Finish")