# song lyric change with input function


    # Function asks the user to input a word to replace a word in the song Come Together by The Beatles
def song_lyric_change():
    print("Provide words to replace in the song 'Come Together' by The Beatles")
    first_word = input("Enter the first word you want to replace: ")
    second_word = input("Enter the second word you want to replace it with: ")
    third_word = input("Enter the third word you want to replace it with: ")
    fourth_word = input("Enter the fourth word you want to replace it with: ")
    fifth_word = input("Enter the fifth word you want to replace it with: ")
    sixth_word = input("Enter the sixth word you want to replace it with: ")
    seventh_word = input("Enter the seventh word you want to replace it with: ")
    eighth_word = input("Enter the eighth word you want to replace it with: ")

    print(f'''Here come {first_word} flat-top, he come {second_word} up {third_word}
    He got {fourth_word} eyeball, he one {fifth_word} roller
    He got {sixth_word} down to his knee
    Got to be a {seventh_word}, he just do what he {eighth_word}
    ''')


# Call the function
song_lyric_change()

# Function is called with single ask with separating commas
def song(a, b, c, d, e, f, g, h):
    print(f'''Here come {a} flat-top, he come {b} up {c}
    He got {d} eyeball, he one {e} roller
    He got {f} down to his knee
    Got to be a {g}, he just do what he {h}
    ''')
        
# Get a single input from the user
lyrics = input("Enter the lyrics you want to change, separated by commas: ")

# Split the input string into individual words
words = lyrics.split(',')

# Call the function with the split words
song(*words)



