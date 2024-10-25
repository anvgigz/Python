def password_validator(password):
    is_valid = True  # Initialize validity as True
    
    # Check if password length is between 8 and 20 characters
    if len(password) < 8 or len(password) > 20:
        print("Password must be between 8 and 20 characters")
        is_valid = False
    
    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        print("Password must contain at least 1 uppercase letter")
        is_valid = False
    
    # Check if password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        print("Password must contain at least 1 lowercase letter")
        is_valid = False
    
    # Check if password contains at least one number
    if not any(char.isdigit() for char in password):
        print("Password must contain at least 1 number")
        is_valid = False
    
    # Check if password contains at least one special character
    if not any(char in "!@#$%&*" for char in password):
        print("Password must contain at least 1 special character (!@#$%&*)")
        is_valid = False
    
    return is_valid  # Return the final validity of the password

def main():
    while True:
        try:
            # Prompt user to enter a password
            password = input("""please enter a password between 8 and 20 characters with at least 1 uppercase,
                                1 lowercase, 1 number, and 1 special character (!@#$%&*) : """)
            
            # Validate the entered password
            if password_validator(password):
                # Prompt user to re-enter the password for confirmation
                re_enter_password = input("Please re-enter your password: ")
                
                # Check if the re-entered password matches the initial password
                if password == re_enter_password:
                    print("Password is successfully created")
                    break  # Exit the loop if the password is valid and confirmed
                else:
                    print("Passwords do not match")
            else:
                print("Password is invalid. Try again")
        except Exception as e:
            print(f"An error occurred: {e}")

# Ensure the program only runs when executed directly
if __name__ == "__main__":
    main()
