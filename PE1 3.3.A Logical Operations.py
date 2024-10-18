def logic():
    # Printing the purpose of the function
    print("Testing logic operators")

    # Calling for user input and adding it to variable number1
    number1 = int(input("Enter a number within the range of 0 - 100: "))

    # Calling for user input and adding it to variable number2
    number2 = int(input("Enter another number within the range of 0 - 100: "))

    # First test: if both numbers are greater than 100
    if number1 > 100 and number2 > 100:
        print(True)  # If both numbers are greater than 100, print True
    else:
        print(False)  # If not, print False

    # Second test: if either number is less than 25
    if number1 < 25 or number2 < 25:
        print(True)  # If either number is less than 25, print True
    else:
        print(False)  # If not, print False

    # Third test: if either number is not within the range of 0 - 100
    if number1 not in range(0, 101) or number2 not in range(0, 101):
        print("You did not type a number within the range of 0 - 100")  # If either number is not between 0-100, print this message
    else:
        print("You typed a number within the range of 0 - 100")  # If both numbers are between 0-100, print this message

# Calling the function to execute the code
logic()
