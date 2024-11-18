# Define the Employee class
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # Getter and Setter for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # Getter and Setter for number
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

# Define the ProductionWorker subclass
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, pay_rate):
        super().__init__(name, number)
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate

    # Getter and Setter for shift_number
    @property
    def shift_number(self):
        return self.__shift_number

    @shift_number.setter
    def shift_number(self, value):
        self.__shift_number = value

    # Getter and Setter for pay_rate
    @property
    def pay_rate(self):
        return self.__pay_rate

    @pay_rate.setter
    def pay_rate(self, value):
        self.__pay_rate = value

    # Method to get shift type as string
    def get_shift_type(self):
        if self.__shift_number == 1:
            return "Day"
        elif self.__shift_number == 2:
            return "Night"
        else:
            return "Unknown"

    # Method to display worker details
    def display_worker_details(self):
        print("-------------------------------------------------------")
        print(f"Name: {self.name}")
        print(f"Employee Number: {self.number}")
        print(f"Shift: {self.get_shift_type()}")
        print(f"Pay Rate: {self.__pay_rate}")
        print("-------------------------------------------------------")


def main():
    print("Enter the following details of the Employee")
    print("--------------------------------------------")
    name = input("Enter Employee Name: ")
    number = input("Enter Employee Number: ")
    pay_rate = float(input("Enter Pay Rate: "))
    shift_number = int(input("Enter Shift Number (1 for day, 2 for night): "))

    # Create an instance of ProductionWorker
    worker = ProductionWorker(name, number, shift_number, pay_rate)

    # Display the worker details
    print("Details of Employee:")
    worker.display_worker_details()

if __name__ == "__main__":
    main()
