class Pet:
    vet_name = "Happy Paws Veterinary Clinic"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getter and Setter for owner_first_name
    @property
    def owner_first_name(self):
        return self.__owner_first_name

    @owner_first_name.setter
    def owner_first_name(self, value):
        self.__owner_first_name = value

    # Getter and Setter for owner_last_name
    @property
    def owner_last_name(self):
        return self.__owner_last_name

    @owner_last_name.setter
    def owner_last_name(self, value):
        self.__owner_last_name = value

    # Getter and Setter for pet_id
    @property
    def pet_id(self):
        return self.__pet_id

    @pet_id.setter
    def pet_id(self, value):
        self.__pet_id = value

    # Getter and Setter for pet_name
    @property
    def pet_name(self):
        return self.__pet_name

    @pet_name.setter
    def pet_name(self, value):
        self.__pet_name = value

    # Getter and Setter for pet_type
    @property
    def pet_type(self):
        return self.__pet_type

    @pet_type.setter
    def pet_type(self, value):
        self.__pet_type = value

    # Method to display pet information
    def display_pet_info(self):
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print(f"Veterinary Clinic: {Pet.vet_name}")

# Function to check property existence
def check_property(pet, property_name):
    return hasattr(pet, property_name)


pet1 = Pet("John", "Doe", 1, "Buddy", "Dog")
pet2 = Pet("Jane", "Smith", 2, "Whiskers", "Cat")
pet3 = Pet("Alice", "Johnson", 3, "Goldie", "Fish")

# Use setter method to change a property
pet3.pet_name = "Goldfish"

# Display pet information
pet1.display_pet_info()
pet2.display_pet_info()
pet3.display_pet_info()

# Check property existence
print(check_property(pet1, "owner_first_name"))  # Should return True
print(check_property(pet2, "owner_middle_name")) # Should return False
