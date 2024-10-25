def main():
    # Step 2: Prompt the user to enter names of flowers and store them in a list
    flowers = []
    print("Enter the names of flowers. Type 'done' when you are finished.")
    while True:
        flower = input("Enter flower name: ")
        if flower.lower() == "done":
            break
        flowers.append(flower)

    # Step 3: Sort the list of flowers and print it with numbers next to each flower
    flowers.sort()
    print("\nSorted list of flowers:")
    for index, flower in enumerate(flowers, start=1):
        print(f"{index}. {flower}")

    # Step 4: Allow the user to search for a specific flower
    search_flower = input("\nEnter the name of the flower to search for: ")
    if search_flower in flowers:
        print(f"{search_flower} is in the list.")
    else:
        print(f"{search_flower} is not in the list.")

    # Step 5: Ask the user for a number to access the corresponding flower
    while True:
        try:
            flower_number = int(input("\nEnter the number of the flower to access: "))
            if flower_number < 1 or flower_number > len(flowers):
                raise IndexError("Invalid number. Please enter a number within the range.")
            print(f"The flower at position {flower_number} is {flowers[flower_number - 1]}.")
            break
        except ValueError:
            print("Please enter a valid number.")
        except IndexError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Step 1: Create a main function to encapsulate the program
if __name__ == "__main__":
    main()