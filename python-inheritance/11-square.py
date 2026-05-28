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
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        print(self.__str__())

    def area(self):
        """Calculates area of square

        Returns: size * size
        """
        return self.__size**2
