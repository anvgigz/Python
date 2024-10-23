# Function to calculate simple interest
def calculate_interest(principal, rate_of_interest, time):
    return (principal * rate_of_interest * time) / 100

# Main program to get user input and print the result
def main():
    principal = float(input("Enter the principal amount: "))
    rate_of_interest = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time (in years): "))
    
    interest = calculate_interest(principal, rate_of_interest, time)
    print(f"The simple interest is {interest:.2f}")

# Call the main function to execute the program
main()
