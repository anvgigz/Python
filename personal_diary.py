def main():
    # Prompt the user to enter the current date and time
    date_time = input("Enter the current date and time (e.g., 2024-11-24 18:30): ")
    # Prompt the user to enter the diary entry
    entry = input("Enter your diary entry: ")
    
    # Define the file path
    file_path = "C:/Users/me/OneDrive/Desktop/python_work/Python Class/diary.txt"
    
    # Open or create the file diary.txt in append mode
    with open(file_path, "a") as file:
        # Write the date and time to the file
        file.write(f"{date_time}\n")
        # Write the diary entry to the file
        file.write(f"{entry}\n")
        # Write a blank line to separate entries
        file.write("\n")

# This calls the main function when the script is executed
if __name__ == "__main__":
    main()
