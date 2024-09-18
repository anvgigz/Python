def creating_a_list():
    names_list = []
    while True:
        print("Please provide your name")
        name = input()
        names_list.append(name)
        if len(names_list) == 5:
            break

    # Convert all names to lowercase
    for i in range(len(names_list)):
        names_list[i] = names_list[i].lower()

    # Bubble sort algorithm
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

creating_a_list()

'''print("Final list of names: \n", names_list)
    print(f"here is the list sorted:\n", sorted(names_list))
    print("here is the list sorted in reverse:\n", sorted(names_list, reverse=True))'''