# triangle.py
import math

def classify_triangle(a, b, c):
    """
    Classifies a triangle based on side lengths a, b, c.
    Returns string like 'scalene', 'isosceles right', etc.
    Assumes valid triangle; no invalid checks for simplicity.
    """
    # Check if right triangle - sort to find hypotenuse
    sides = sorted([a, b, c])
    x, y, z = sides
    if math.isclose(x**2 + y**2, z**2, rel_tol=1e-9):
        right = " right"
    else:
        right = ""
    
    # Classify shape
    if a == b == c:
        shape = "equilateral"
    elif a == b or b == c or a == c:
        shape = "isosceles"
    else:
        shape = "scalene"
    
    return shape + right
