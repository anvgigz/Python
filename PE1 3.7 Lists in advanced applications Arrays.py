days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["morning", "afternoon", "evening"]

# Initialize a list to store heart rates for each day and time of day
heart_rates = []

for day in days:
    day_rates = []  # Initialize a sublist for the current day
    for time in time_of_day:
        while True:
            try:
                heart_rate_input = int(input(f"What was your heart rate on {day} in the {time}? "))
                # Store the time slot and heart rate as a sublist
                day_rates.append([time, heart_rate_input])
                break
            except ValueError:
                print("Please enter a valid number.")
    heart_rates.append([day, day_rates])  # Append the sublist to the main list

# Calculate average heart rate
total_heart_rate = sum(rate for day in heart_rates for time, rate in day[1])
average = total_heart_rate / (len(days) * len(time_of_day))

# Print the recorded heart rates for each day and time of day
print("\nHeart rate recorded for each day and time of day:")
for day, rates in heart_rates:
    print(f"{day}:")
    for time, rate in rates:
        print(f"  {time}: {rate}")

print(f"\nAverage heart rate: {average:.2f}")
