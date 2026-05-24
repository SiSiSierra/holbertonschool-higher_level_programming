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
        number_of_instances
        print_symbol

    Functions:
        area(): Calculate area
        perimeter(): Calculate perimeter
        bigger_or_equal(rect_1, rect_2)
    """

    """ Class data """

    number_of_instances = 0
    print_symbol = '#'

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    """ Instance data """

    def __str__(self):
        if self.width == 0:
            return ""
        out = ""
        for i in range(self.height):
            out += str(self.print_symbol) * self.width
            if i + 1 != self.height:
                out += "\n"
        return out

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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
