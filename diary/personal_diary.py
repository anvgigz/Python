import os

def main():
    # Prompt the user to enter the current date and time
    date_time = input("Enter the current date and time (e.g., 2024-11-23 18:30): ")
    # Prompt the user to enter the diary entry
    entry = input("Enter your diary entry: ")
    
    # Define the file name (without an explicit path)
    file_name = "diary.txt"

    try:
        # Open the file in append mode
        with open(file_name, "a") as file:
            # Write the date and time to the file
            file.write(f"{date_time}\n")
            # Write the diary entry to the file
            file.write(f"{entry}\n")
            # Write a blank line to separate entries
            file.write("\n")
    except Exception as e:
        print(f"An error occurred: {e}")

# This calls the main function when the script is executed
if __name__ == "__main__":
    main()
