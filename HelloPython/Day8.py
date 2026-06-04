"""
Day 8 — Dictionary Basics
Problem: Create a dictionary representing a person's profile:

Keys: name, age, city, occupation
Print each key-value pair using a loop.
Add a new key email.
Update the city to a different city.
Delete the occupation key.
Check if "phone" exists in the dictionary. Print a message either way.
Concepts: Dictionary creation, keys(), values(), items(), del, in
"""

profile = {
    'Name' : 'Sanjay Raghuwanshi',
    'Age' : '34',
    'City' : 'Pune',
    'Occupation' : 'Engineer'
    }

#print(profile['occupation'])

# Print each key value pair using a loop
for key, val in profile.items():
    print(f"{key}: {val}")

#Print only the key of the dictionary
print(profile.keys())

#Print only the values of the dictionary
print(profile.values())

# Add a new key email
profile['Email'] = 'raghu1c.sanjay@gmail.com'
print(profile)

# Update the city to a different city
profile.update({'City': 'Bhopal'})
#print(profile)

# Delete the occupation key.
profile.pop('Occupation')
# del profile['City']  <- can use del as well.
#print(profile)

# Check if "phone" exists in the dictionary. Print a message either way.
print(profile.get('Phone','None'))
