import pytest
import doctest
import unittest

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
def area(width, height):
    """
    Calculate the area of a rectangle.

    >>> area(3, 4)
    12

    >>> area(5, 5)
    25
    """
    return width * height

if __name__ == "__main__":
    doctest.testmod()

class TestRectangle(unittest.TestCase):
    def test_area(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)

        rectangle = Rectangle(5, 5)
        self.assertEqual(rectangle.area(), 25)

    def test_perimeter(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.perimeter(), 14)

        rectangle = Rectangle(5, 5)
        self.assertEqual(rectangle.perimeter(), 20)

if __name__ == "__main__":
    unittest.main()

@pytest.fixture
def rectangle():
    return Rectangle(3, 4)

def test_area(rectangle):
    assert rectangle.area() == 12

def test_perimeter(rectangle):
    assert rectangle.perimeter() == 14
