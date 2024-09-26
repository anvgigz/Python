#Assignment: Simple Interest Calculator
#Objective: Write a Python function named calculate_interest 
# that computes and returns the simple interest based on given parameters.

def calculate_interest(principle,rate_of_interest,time):
    simple_interest = (principle * rate_of_interest * time) / 100
    print(f"The simple interest is {simple_interest}")

calculate_interest(1000, 5, 2)