#functions to be called area_of_triangle, area_of_circle, area_of_rectangle


def area_of_triangle(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def area_of_circle(radius):
    """Calculate the area of a circle."""
    pi = 3.141592653589793
    return pi * (radius ** 2)

def area_of_rectangle(length, width):
    """Calculate the area of a rectangle."""
    return length * width