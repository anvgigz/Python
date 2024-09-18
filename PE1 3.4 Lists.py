days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
steps = []

for day in days:
    while True:
        try:
            step_count = int(input(f"How many steps did you take on {day}? "))
            steps.append(step_count)
            break
        except ValueError:
            print("Please enter a valid number.")

print("\nSteps recorded for each day:")
for day, step in zip(days, steps):
    print(f"{day}: {step} steps")

total_steps = sum(steps)
print(f"\nTotal steps taken in the week: {total_steps}")

average_steps = round(total_steps / len(steps))
print(f"Average steps taken per day: {average_steps}")




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

