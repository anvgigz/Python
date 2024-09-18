print("Hello can you please tell me your age so I can determine if you can or cannot drive")
age = int(input("Please enter your age: ")) # user needs to input a number or the program crashes
if age >= 16: 
    print("You are old enough to drive") # greater than or equal to 16 will execute this print statement
else:
    print("You are not old enough to drive") # less then 16 will execute this print statement

if age >= 18: 
    print("You are old enough to vote") # greater than or equal to 18 will execute this print statement
else:
    print("You are not old enough to vote")# less than 18 will execute this print statement
if  age >= 21: 
    print("You are old enough to drink")# greater than or equal to 21 will execute this print statement
else:
    print("You are not old enough to drink")# less than 21 will execute this print statement

if age >= 65:
    print(" You are old enough to get a senior discount") # greater than or equal to 65 will execute this print statement
else:
    print("You are not old enough to get a senior discount") # less than 65 will execute this print statement

