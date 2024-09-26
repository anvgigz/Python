#Functions for finding the area of a circle and square

#Square function

def area_of_square(a,b): #calling the function with two parameters needing to be used
    area = a*b
    print(f"The area of the square is {area}")

area_of_square(5,5)#Function called and executed

#area of circle
def area_of_circle(r):
    area = 3.14 * r**2
    print(f"The area of the circle is {area}")

area_of_circle(5)#Function called and executed
