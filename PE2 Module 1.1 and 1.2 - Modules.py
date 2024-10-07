#Assignment: Number Guessing Game

import random #random imported to generate random numbers

def guessing_game():
    print("this is the guessing game please input a number between 1 and 100")
    answer = False
    number_generated = random.randint(1,100) # generates a random number between 1 and 100
    while answer is False:
        try:
            guess = int(input())
            if guess == number_generated:
                print("You got it right")       # answer correctly guessed // answer is turned to True to break the loop.
                answer = True
            elif guess > number_generated:      # lets the user know their number is too high // function will call itself again
                print("Your guess is too high")
            elif guess < number_generated:  # lets the user know their number is too low // function will call itself again
                print("Your guess is too low")
        except ValueError:      # if the user enters a string instead of a number. function will call itself again
            print("Please enter a number you did not do that")
            continue

guessing_game() # call function
