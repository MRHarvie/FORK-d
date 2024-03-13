class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def speak(self):
        print("No Animal? No Sound!")

class Dog(Animal):
    def __init__(self,name,species,breed):
        Animal.__init__(self,name,species)
        self.breed = breed
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self,name,species,colour):
        Animal.__init__(self,name,species)
        self.colour = colour

    def speak(self):
        print("Meow!")

dog = Dog("Max", "Dog", "Golden Retriever")
cat = Cat("Whiskers", "Cat", "Orange")

print("Dog:")
print("Name:", dog.name)
print("Species:", dog.species)
print("Breed:", dog.breed)
print("Sound:", end=" ")
dog.speak()
print("\n")

print("Cat:")
print("Name:", cat.name)
print("Species:", cat.species)
print("Colour:", cat.colour)
print("Sound:", end=" ")
cat.speak()