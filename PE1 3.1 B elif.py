print("what grade did you get on your test:")
grade = int(input())
print(f"So you scored a {grade}, let me check the grade boundaries")


def grading_rubric():
    if grade >= 90:
        print("You got an A")
    elif 80 <= grade < 90:
        print("You got a B") 
    elif 70 <= grade < 80:
        print("You got a C")
    elif 60 <= grade <70:
        print("You got a D")
    else:
        print("You got an F")

grading_rubric()