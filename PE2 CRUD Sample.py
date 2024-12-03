import re

def main_menu():
    print("Menu:")
    while True:
        try:
            print("\n\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")

def check():
    try:
        with open("customer_list.txt", 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []



def create():
    customer = check()

    while True:
        fname = input("Please enter the customer\'s first name: ").strip()
        if fname.isalpha():
            break
        else:
            print("First name must only contain letters. Please try again.")

    while True:
        lname = input("Please enter the customer\'s last name: ").strip()
        if lname.isalpha():
            break
        else:
            print("Last name must only contain letters. Please try again.")

    while True:
        phone = input("Please enter the customer\'s phone: ").strip()
        if re.fullmatch(r'\d{10}', phone):  # Validates a 10-digit phone number
            break
        else:
            print("Phone number must be a 10-digit number. Please try again.")

    while True:
        email = input("Please enter the customer\'s email: ").strip()
        if re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email):  # Basic email validation
            break
        else:
            print("Invalid email format. Please try again.")

    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)

    try:
        save(customer)
    except Exception as e:
        print(f"An error occurred while saving: {e}")


def read():
    customers = check()
    lname = input("Enter the last name of the customer you wish to find: ").strip()
    found = False
    for customer in customers:
        if lname in customer:
            print("Entry found:", customer)
            found = True
    if not found:
        print("No entry found for the last name:", lname)

import re

def update():
    customers = check()
    lname = input("Enter the last name of the customer you wish to update: ").strip()
    found = False
    for i, customer in enumerate(customers):
        if lname in customer:
            print("Current entry:", customer)
            
            while True:
                fname = input("Enter new first name: ").strip()
                if fname.isalpha():
                    break
                else:
                    print("First name must only contain letters. Please try again.")

            while True:
                phone = input("Enter new phone: ").strip()
                if re.fullmatch(r'\d{10}', phone):  # Validates a 10-digit phone number
                    break
                else:
                    print("Phone number must be a 10-digit number. Please try again.")

            while True:
                email = input("Enter new email: ").strip()
                if re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email):  # Basic email validation
                    break
                else:
                    print("Invalid email format. Please try again.")

            customers[i] = f"{fname}, {lname}, {phone}, {email}\n"
            
            try:
                save(customers)
            except Exception as e:
                print(f"An error occurred while saving: {e}")
            
            print("Entry updated.")
            found = True
            break
    if not found:
        print("No entry found for the last name:", lname)


def delete():
    customers = check()
    lname = input("Enter the last name of the customer you wish to delete: ").strip()
    found = False
    for customer in customers:
        if lname in customer:
            customers.remove(customer)
            save(customers)
            print("Entry deleted.")
            found = True

            break
    if not found:
        print("No entry found for the last name:", lname)

def save(output):
    with open("customer_list.txt", 'w') as file:
        for line in output:
            file.write(line)
    print("File updated.")

def main():
    while True:
        choice = main_menu()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
