class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.species}.")

dog = Pet(name="Buddy", species="Dog")
cat = Pet(name="Whiskers", species="Cat")

print(f"{dog.name}, {dog.species}")
print(f"{cat.name}, {cat.species}")

dog.introduce()
cat.introduce()