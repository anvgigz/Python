# Define the function that takes 8 parameters
def custom_song(noun1, verb1, verb2, adjective1, noun2, body_part, noun3, action):
    print(f'''
    Here come {noun1} flat-top, he come {verb1} up {verb2}
    He got {adjective1} eyeball, he one {noun2} roller
    He got {body_part} down to his knee
    Got to be a {noun3}, he just do what he {action}
    ''')

# Collect user input for each of the 8 variables with clear and descriptive prompts
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
adjective1 = input("Enter an adjective: ")
noun2 = input("Enter another noun: ")
body_part = input("Enter a body part: ")
noun3 = input("Enter another noun: ")
action = input("Enter an action: ")

# Call the function with the user inputs as named arguments
custom_song(noun1, verb1, verb2, adjective1, noun2, body_part, noun3, action)
