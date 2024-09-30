#Assignment: NATO Phonetic Alphabet Dictionary

# Step 1: Create the NATO Phonetic Alphabet Dictionary
nato_alphabet = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
    "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"
}

# Step 2: Develop the Spelling Program
def spell_word():
    user_word = input("Enter a word: ").upper()  # Convert to uppercase to match dictionary keys
    for letter in user_word:
        if letter in nato_alphabet:
            print(nato_alphabet[letter])
        else:
            print(f"'{letter}' is not a valid letter in the NATO Phonetic Alphabet.")

# Step 3: Incorporate a Main Function
def main():
    spell_word()

# Step 4: Test Your Program
if __name__ == "__main__":
    main()
