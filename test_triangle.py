# test_triangle.py
import unittest
import math
from triangle import classify_triangle

class TestTriangleClassification(unittest.TestCase):
    
    def test_equilateral(self):
        self.assertEqual(classify_triangle(2, 2, 2), "equilateral")
    
    def test_isosceles_not_right(self):
        self.assertEqual(classify_triangle(2, 2, 1), "isosceles")
    
    def test_scalene_not_right(self):
        self.assertEqual(classify_triangle(3, 4, 6), "scalene")
    
    def test_isosceles_right(self):
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "isosceles right")
    
    def test_scalene_right(self):
        self.assertEqual(classify_triangle(3, 4, 5), "scalene right")

if __name__ == '__main__':
    unittest.main()
