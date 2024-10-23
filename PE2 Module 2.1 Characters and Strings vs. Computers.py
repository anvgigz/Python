def main():
    # Prompt the user to enter a character
    user_input = input("Enter a character: ")

    # Loop to ensure the user enters exactly one character
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")

    # Get the ASCII value of the entered character
    ascii_value = ord(user_input)

    # Print the ASCII value
    print(f"The ASCII value of {user_input} is {ascii_value}")

# Call the main function to execute the program
main()
