import math

print(math.hypot(9,12) == math.sqrt(225))
True

print(math.trunc(7.3) == math.floor(7.4))
True

print(math.floor(10.8) > math.ceil(10.8))
False

print(math.factorial(3) == math.pow(3, 2))
False

print(math.ceil(math.pi))
# 4

###
# Open the file is_triangle.py, and fix the function
# so that it returns True when the side c is the longest
# side of a right-angled triangle.
# Note: right-angled triangle, or more formally an orthogonal
# triangle is a triangle in which one angle is a 90-degree angle.


def is_triangle(a, b, c):
    if math.hypot(a, b) == c:
        return True
    return False


print("The program checks if three sides form a right-angled triangle.")
inp1 = int(input("Enter first side value: "))
inp2 = int(input("Enter second side value: "))
inp3 = int(input("Enter third side value: "))
print("Is triangle?", is_triangle(inp1, inp2, inp3))

###
# Open the file trigonometry.py, and complete
# the function that calculates the area of
# a circle given a user's input as radius.
# Do any necessary imports here
import math

# Complete the function
def circle_area(r):
    return math.pi * r * r


inp = float(input("Enter the radius of a circle:"))
print("Area of circle =", circle_area(inp))