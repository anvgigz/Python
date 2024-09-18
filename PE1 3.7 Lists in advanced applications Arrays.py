days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["morning", "afternoon", "evening"]

# Initialize a list to store heart rates for each day and time of day
heart_rate = [[None for _ in time_of_day] for _ in days]

for day_index, day in enumerate(days):
    for time_index, time in enumerate(time_of_day):
        while True:
            try:
                heart_rate_input = int(input(f"What was your heart rate on {day} in the {time}? "))
                # Append the heart rate to the corresponding time of day for the current day
                total_heart_rate = []
                total_heart_rate.append(heart_rate_input)
                
                heart_rate[day_index][time_index] = heart_rate_input
                break
            except ValueError:
                print("Please enter a valid number.")
average = sum(total_heart_rate) / len(total_heart_rate)
# Print the recorded heart rates for each day and time of day
print("\nHeart rate recorded for each day and time of day:")
for day_index, day in enumerate(days):
    print(f"{day}:")
    for time_index, time in enumerate(time_of_day):
        print(f"  {time}: {heart_rate[day_index][time_index]}")

print(f"Average heart rate: {average}")












# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# time_of_day = ["morning", "afternoon", "evening"]

# # Initialize a dictionary to store heart rates for each day and time of day
# heart_rate = {day: {} for day in days}

# for day in days:
#     for time in time_of_day:
#         while True:
#             try:
#                 heart_rate_input = int(input(f"What was your heart rate on {day} in the {time}? "))
#                 # Append the heart rate to the corresponding time of day for the current day
#                 heart_rate[day][time] = heart_rate_input
#                 break
#             except ValueError:
#                 print("Please enter a valid number.")

# # Print the recorded heart rates for each day and time of day
# print("\nHeart rate recorded for each day and time of day:")
# for day, times in heart_rate.items(): #items() is used for listing key and value items.
#     print(f"{day}: {times}")

