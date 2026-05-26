customer = \
    {'name': 'John Smith',
     'age': 30,
     'is_verified': True }
print(customer["name"])
#use get method to check if the key exists in dictionary
print(customer.get("birthdate"))

#Assign a default value to a non-existing key
print(customer.get("birthdate", "Jan 1 1980"))