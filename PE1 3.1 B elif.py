print("what grade did you get on your test:")
grade = int(input()) #user needs to input a number or the progeram crashes
print(f"So you scored a {grade}, let me check the grade boundaries")


def grading_rubric():
    if grade >= 90: #if greater than 90 the grade is an A
        print("You got an A")
    elif 80 <= grade < 90: #If between 80 and 89 Grade is B
        print("You got a B") 
    elif 70 <= grade < 80: #if Between 70 and 79 Grade is a C
        print("You got a C")
    elif 60 <= grade <70: #If between 60 and 69 grade is D
        print("You got a D")
    else:
        print("You got an F") #anything below 60 is an F

grading_rubric()
