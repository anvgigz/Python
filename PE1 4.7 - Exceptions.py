# Simple Python program to calculate the square of a number
def square_number():
    while True:  # Loop until a valid number is entered
        try:
            number = input("Enter a number to square: ")
            squared_number = int(number) ** 2
            print(f"The square of {number} is {squared_number}.")
            break  # Exit loop if no errors
        except ValueError:  # Catch non-numeric input errors
            print("Please enter a valid number.")

# Call the function
square_number()
