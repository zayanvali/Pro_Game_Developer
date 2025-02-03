## Object Oriented Programming Concepts in Python

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)
print(dog1.age) 
print(dog1.species)

print("\n")

class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)

print("\n")



# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")

# Example Usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name} Guides the way!")


guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()


# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Friendly, Dog):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()

