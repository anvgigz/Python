import calendar
from datetime import datetime

def main():
    # Get the current year
    current_year = datetime.now().year
    
    while True:
        try:
            # Ask the user to enter their birth month
            birth_month = int(input("Enter your birth month (as a number between 1 and 12): "))
            
            # Validate the user input to ensure it's an integer between 1 and 12
            if birth_month < 1 or birth_month > 12:
                raise ValueError("Month must be between 1 and 12.")
            
            # If valid, break out of the loop
            break
        except ValueError as e:
            # Handle invalid input gracefully by displaying an error message
            print(f"Invalid input: {e}. Please try again.")
    
    # Generate the calendar for the given month and year
    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_calendar = cal.formatmonth(current_year, birth_month)

    # Print the calendar to the console in a readable format
    print("\nHere's your birth month calendar for the current year:\n")
    print(month_calendar)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
