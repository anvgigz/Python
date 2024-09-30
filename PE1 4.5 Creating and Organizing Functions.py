#Assignment: Calculating Factorials

def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n - 1)
    
def main():
    while True:
        try:
            n = int(input("Enter a non-negative number: "))
            if n < 0:
                print("Please enter a non-negative number.")
            else:
                number = factorial(n)
                print(f"The factorial of {n} is {number}")
                break  # Exit the loop if input is valid
        except ValueError:
            print("Please enter a valid number.")

if __name__ =="__main__":
    main()