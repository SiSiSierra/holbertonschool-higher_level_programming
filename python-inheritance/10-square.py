#!/usr/bin/python3
"""Module

Classes:
    Square(Rectangle)
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a square shape

    Functions:
        area(self)
    """
    def __init__(self, size):
        super().__init__(size, size)

    def area(self):
        """Calculates area of square

        Returns: size * size
        """
        return super().area()
