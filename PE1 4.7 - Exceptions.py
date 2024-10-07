#Assignment: Adding Exception Handling

score = 0

def previus_score():
    global score
    try:
        print("input your previus score")
        old_score = int(input())
        score = old_score
        print("Your previus score has been added: ", score)
    except ValueError:
        print("Please enter a number")
        previus_score()

previus_score()

