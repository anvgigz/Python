def two_letter_combinations(characters):
    """
    Generator function that yields all possible two-letter combinations 
    from a given list of characters.
    """
    # Iterate over each character in the list for the first position
    for first_char in characters:
        # Iterate over each character in the list for the second position
        for second_char in characters:
            # Yield the combination of the two characters
            yield first_char + second_char

def main():
    # Define a list of characters (example with 5 letters)
    char_list = ['a', 'b', 'c']

    # Call the generator function and print each combination
    for combination in two_letter_combinations(char_list):
        print(combination)

# Run the main function
main()
