days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
steps = []  # Empty list to append steps

for day in days:  # Each day in list days will be executed in the loop
    try:
        step_count = int(input(f"How many steps did you take on {day}? "))
        steps.append(step_count)  # Append the step count to the list
    except ValueError:
        print("Please enter a valid number.")

print("\nSteps recorded for each day:")  # After the loop is completed, the code continues here
for day, step in zip(days, steps):  # The zip function is used to pair the days with steps accordingly
    print(f"{day}: {step} steps")  # Printed ex - Monday: 2000 steps

total_steps = sum(steps)  # The sum function adds all the steps together using addition and puts them into the variable total_steps
print(f"\nTotal steps taken in the week: {total_steps}")  # Total steps is printed in an f-string

average_steps = round(total_steps / len(steps))  # The total steps is divided by the number of days in steps
# This number is then rounded using the round function which provides an integer rather than a float
print(f"Average steps taken per day: {average_steps}")  # Average per week is printed
