class NotNumericError(Exception):
    def __init__(self, message="Input is not a number"):
        self.message = message
        super().__init__(self.message)



def main():
    while True:
        try:
            # Prompt the user for input
            user_input = input("Please enter a number: ")
            
            # Check if the input is numeric
            if not user_input.isnumeric():
                raise NotNumericError
            
            # If the input is valid, print confirmation
            else:
                print(f"Thank you! You entered the number: {user_input}")
                break
        
        except NotNumericError as e:
            # Handle the invalid input
            print(f"Error: {e.message}")
        
        finally:
            # Indicate the end of this iteration
            print("End of this iteration.\n")
            
    print("End of program.")

if __name__ == "__main__":
    main()
