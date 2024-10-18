print("What grade did you get on your test:")
grade = int(input()) # Ensure the user inputs a number to avoid crashing

print(f"So you scored a {grade}, let me check the grade boundaries")

def grading_rubric():
    if grade >= 90:
        print("You got an A")
    elif grade >= 80:
        print("You got a B")
    elif grade >= 70:
        print("You got a C")
    elif grade >= 60:
        print("You got a D")
    else:
        print("You got an F")  # Anything below 60 is an F

grading_rubric()
