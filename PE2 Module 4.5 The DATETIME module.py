from datetime import datetime

def main():
    print("\n\n")
    try:
        # Get the current date
        today = datetime.today()
        
        # Get the user's birth year, month, and day
        birth_year = int(input("What year were you born?  "))
        month = int(input("What month were you born (as a number. May would be 5)?  "))
        day = int(input("What day of the month were you born?  "))
        
        # Create a datetime object for the user's birthday
        birthday = datetime(birth_year, month, day)
        print("Your birthday is:")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 

        # Calculate the difference between today and the birthday
        delta = today - birthday
        print(f'Difference is {delta.days} days')

        # Calculate the age in years (considering leap years by dividing by 365.2425)
        delta_years = delta.days / 365.2425
        print(f'You are {delta_years:.2f} years old')
        
        # Calculate the age in months (using an average of 30.41 days per month)
        delta_months = delta.days / 30.41
        print(f'You are approximately {delta_months:.2f} months old')

        # Calculate the age in weeks
        delta_weeks = delta.days / 7
        print(f'You are approximately {delta_weeks:.2f} weeks old')

        # Calculate the age in days (this is already provided by delta.days)
        delta_days = delta.days
        print(f'You are {delta_days} days old')

        # Calculate the age in hours (24 hours per day)
        delta_hours = delta_days * 24
        print(f'You are approximately {delta_hours:,} hours old')

        # Calculate the age in minutes (60 minutes per hour)
        delta_minutes = delta_hours * 60
        print(f'You are approximately {delta_minutes:,} minutes old')

    except Exception as e:
        print(f"Oops!!!: {e}") 
        main()

# Call the main function to execute the program
if __name__ == "__main__":
    main()
