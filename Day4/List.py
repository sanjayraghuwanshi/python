#List

fruits = ["Cherry", "Apple", "Pear"]

print(fruits[0]) # It'll print Cherry in the output
print(fruits[1]) # It'll print Apple in the output
print(fruits[2]) # It'll print Pear in the output

print(fruits[-1]) # It'll print Pear in the output
print(fruits[-2]) # It'll print Apple in the output

fruits[1] = "Mango" # It'll replace Apple with Mango
print(fruits)

fruits.append("Guava")  # It'll append the list with new item Guava
print(fruits)
#output - ['Cherry', 'Mango', 'Pear', 'Guava']

fruits.extend(["Guava","Tomato"]) # It'll extend the list with new item Guava and Tomato
print(fruits)
#output - ['Cherry', 'Mango', 'Pear', 'Guava', 'Guava', 'Tomato']

