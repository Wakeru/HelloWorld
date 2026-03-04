"""Triangle classification functions."""

import math


def classify_triangle(a, b, c):
    """
    Classify a triangle based on side lengths a, b, c.

    Returns:
        str: One of 'equilateral', 'isosceles', 'scalene' with optional ' right'.
    """
    sides = sorted([a, b, c])
    x, y, z = sides

    if math.isclose(x**2 + y**2, z**2, rel_tol=1e-9):
        right = " right"
    else:
        right = ""

    if a == b == c:
        shape = "equilateral"
    elif a == b or b == c or a == c:
        shape = "isosceles"
    else:
        shape = "scalene"

    return shape + right
