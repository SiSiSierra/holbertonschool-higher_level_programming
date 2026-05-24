#!/usr/bin/python3
"""Module defining a rectangle class

Classes:
    Rectangle: Defines a rectangle
"""


class Rectangle():
    """Rectangle class

    Attributes:
        __width
        __height

    Functions:
        area(): Calculate area
        perimeter(): Calculate perimeter
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        if self.width == 0:
            return ""
        out = ""
        for i in range(self.height):
            out += "#" * self.width
            if i + 1 != self.height:
                out += "\n"
        return out

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)
