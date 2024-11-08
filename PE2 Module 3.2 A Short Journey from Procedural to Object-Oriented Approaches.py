class Person:
    def __init__(self, name, address, age, phone):
        #Private variables udsing 2 __ before the name
        self.__name = name 
        self.__address = address
        self.__age = age
        self.__phone = phone

    # Accessor methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    # Mutator methods
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone


# Creating instances of the Person class
person1 = Person("John Doe", "123 Maple Street", 25, "555-1234")
person2 = Person("Jane Smith", "456 Oak Avenue", 30, "555-5678")
person3 = Person("Emily Johnson", "789 Pine Road", 22, "555-9101")

# Displaying data for each instance
def print_person_info(person):
    print(f"Name: {person.get_name()}")
    print(f"Address: {person.get_address()}")
    print(f"Age: {person.get_age()}")
    print(f"Phone: {person.get_phone()}")
    print("---------------------------")

print_person_info(person1)
print_person_info(person2)
print_person_info(person3)

person1.set_name("John Smith")
print("Person1 Edited")
print_person_info(person1)
