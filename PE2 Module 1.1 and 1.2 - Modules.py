#Assignment: Number Guessing Game

import random #random imported to generate random numbers

def guessing_game():
    print("this is the guessing game please input a number between 1 and 100")
    answer = False
    number_generated = random.randint(1,100) # generates a random number between 1 and 100
    while answer is False:
        try:
            guess = int(input())
            difference = abs(number_generated - guess) # finds the difference between the generated number and the guessed number
            if guess == number_generated:
                print("Congratulations you guessed right")
                answer = True
            elif difference <= 5:   # if value guessed is less then or equal to the difference this wil be printed // stating how far away you are from the guess
                print(f"Very hot. Difference: {difference}")
            elif difference <= 15:  # if value guessed is less then or equal to the difference this wil be printed // stating how far away you are from the guess
                print(f"Hot. Difference: {difference}")
            elif difference <= 25:  # if value guessed is less then or equal to the difference this wil be printed // stating how far away you are from the guess
                print(f"Cool. Difference: {difference}")
            else:   # rather than doing a greater than sign for 25 an else statement will suffice and number of fdifference will be printed.
                print(f"Cold. Difference: {difference}")
           
        except ValueError:      # if the user enters a string instead of a number. function will call itself again
            print("Please enter a number you did not do that")
            continue

guessing_game() # call function
