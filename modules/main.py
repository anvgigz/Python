from math_operations import calculator ,geometry    # functions from calculator.py and geometry.py are imported for use.
#calculator.function name must be called to use the functions in calculator.py
#gerometry.function name must be called to use the functions in geometry.py



result = calculator.add(5, 3)
print("Addition result:", result)

result = calculator.subtract(10, 4)
print("Subtraction result:", result)

result = geometry.area_of_triangle(3,8)
print("Area of triangle:", result)

result = geometry.area_of_circle(15)
print("Area of circle:", result)

result = geometry.area_of_rectangle(15,12)
print("Area of rectangle:", result)