def main():
    file_name = "sales_totals.txt"

    try:
        # Initialize variables for total and count
        total = 0.0
        count = 0

        # Open the file in read mode
        with open(file_name, "r") as file:
            # Read in all lines using a loop
            for line in file:
                # Strip the newline symbol and convert each line to a float
                number = float(line.strip())
                
                # Add each number to the running total
                total += number
                
                # Count the number of lines
                count += 1
                
                # Format and display each number
                print(f"{number:,.2f}")

        # Outside of the loop, format and display the total, the count, and the average
        average = total / count if count != 0 else 0
        print(f"\nTotal: {total:,.2f}")
        print(f"Number of entries: {count}")
        print(f"Average: {average:,.2f}")

    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except ValueError:
        print("Error: One of the lines in the file could not be converted to a float.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# This calls the main function when the script is executed
if __name__ == "__main__":
    main()
