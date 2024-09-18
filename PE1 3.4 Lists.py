days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
steps = [] # empty list ot append steps

for day in days: # each day in list days will be executed in the while loop
    while True:
        try:
            step_count = int(input(f"How many steps did you take on {day}? "))
            steps.append(step_count)
            break # used to move loop to next day
        except ValueError:
            print("Please enter a valid number.")

print("\nSteps recorded for each day:") # after the while loop completed the code continues here
for day, step in zip(days, steps): # the zip function is used to pair the days with steps accordingly based on the order the they were input
    print(f"{day}: {step} steps") #printeed ex - Monday: 2000 steps

total_steps = sum(steps)  # the sum function adds all the steps together usign addition. and puts them into the variable total_steps
print(f"\nTotal steps taken in the week: {total_steps}") #  # total_steps is printed in an f-string

average_steps = round(total_steps / len(steps)) # the total steps is divided by the amount of numbers in steps( which would be 7 based off the while loop of days of the week
# This number is then rounded using the round function which provides an integer rather than a float
print(f"Average steps taken per day: {average_steps}") # average per week is printed




"""Got ahead of myself VVVVVVVVVvv"""

# global_list = [1,2,3,4,5,6,7,8,9,10,11,12]

# class lists():

 
#     def append_list():
#         global global_list
#         for number in range(13, 101):
#             global_list.append(number)
#         print(f"printing the list\n{global_list}\n")

#     def removing_numbers():
#         global global_list
#         for number in global_list:
#             if number % 2 ==0:
#                 global_list.remove(number)
#         print(f"printing the list\n{global_list}\n")

#     def reverse_sort():
#         global global_list
#         global_list.reverse()
#         print(f"printing the list\n{global_list}\n")

#     def pop_list():
#         global global_list
#         global_list.pop()
#         print(f"printing the list\n{global_list}\n")

#     def len_list():
#         global global_list
#         print(f"printing the length of the list\n{len(global_list)}\n")

#     def sort_list():
#         global global_list
#         global_list.sort()
#         print(f"printing the list\n{global_list}\n")
    


# lists.append_list()
# lists.removing_numbers()
# lists.reverse_sort()
# lists.pop_list()
# lists.len_list()
# lists.sort_list()

