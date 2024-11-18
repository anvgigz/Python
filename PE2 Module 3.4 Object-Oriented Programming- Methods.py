# Pet class definition
class Pet:
    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    # Getter and Setter for kind
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    # Getter and Setter for breed
    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, value):
        self.__breed = value

    # Getter and Setter for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # Method to print the details of the pet
    def print_details(self):
        print(f"Pet Kind: {self.__kind}")
        print(f"Pet Breed: {self.__breed}")
        print(f"Pet Name: {self.__name}")

# Creating instances of the Pet class
pet1 = Pet("Dog", "Golden Retriever", "Buddy")
pet2 = Pet("Cat", "Siamese", "Whiskers")
pet3 = Pet("Fish", "Goldfish", "Goldie")

# Calling print_details for each object
pet1.print_details()
print()
pet2.print_details()
print()
pet3.print_details()
print()

# Demonstrate the use of the special method `type()`
print(f"Type of pet1: {type(pet1)}")  # Should show that pet1 is an instance of the Pet class
print(f"Type of pet2: {type(pet2)}")  # Should show that pet2 is an instance of the Pet class
print(f"Type of pet3: {type(pet3)}")  # Should show that pet3 is an instance of the Pet class

# Include comments to demonstrate the usage of the special method
# The type() function returns the class type of the given object, in this case, instances of the Pet class
