def creating_a_list():
    # Initialize an empty list to store names
    names_list = []

    # Loop to collect 5 names from the user
    while len(names_list) < 5:
        print("Please provide your name")
        name = input()
        names_list.append(name)

    # Convert all names to lowercase for consistent sorting
    for i in range(len(names_list)):
        names_list[i] = names_list[i].lower()

    # Bubble sort algorithm to sort the names in alphabetical order
    swapped = True
    while swapped:
        swapped = False  # Reset the flag at the start of each iteration
        for i in range(len(names_list) - 1):
            # Compare adjacent elements
            if names_list[i] > names_list[i + 1]:
                swapped = True  # A swap is needed
                # Swap the elements
                names_list[i], names_list[i + 1] = names_list[i + 1], names_list[i]

    # Print the sorted list
    print("Sorted list:", names_list)

    # Reverse the list and print it
    names_list.reverse()
    print("Reversed list:", names_list)

# Call the function to execute the code
creating_a_list()
