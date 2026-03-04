"""Unit tests for triangle.classify_triangle()."""

import math
import unittest

from triangle import classify_triangle


class TestTriangleClassification(unittest.TestCase):
    """Tests for triangle classification results."""

    def test_equilateral(self):
        """Equilateral triangles have three equal sides."""
        self.assertEqual(classify_triangle(2, 2, 2), "equilateral")

    def test_isosceles_not_right(self):
        """Isosceles (not right) triangles should not include 'right'."""
        self.assertEqual(classify_triangle(2, 2, 1), "isosceles")

    def test_scalene_not_right(self):
        """Scalene (not right) triangles should not include 'right'."""
        self.assertEqual(classify_triangle(3, 4, 6), "scalene")

    def test_isosceles_right(self):
        """Isosceles right triangle should return 'isosceles right'."""
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "isosceles right")

    def test_scalene_right(self):
        """3-4-5 is a classic right scalene triangle."""
        self.assertEqual(classify_triangle(3, 4, 5), "scalene right")


if __name__ == "__main__":
    unittest.main()
