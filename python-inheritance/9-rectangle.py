#!/usr/bin/python3
"""Module

Classes:
    Rectangle(BaseGeometry)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class defining a shape

    Inherits: BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        print(self.str())

    def area(self):
        """Defines the area of the rectangle

        Returns: width * height to get area
        """
        return self.__width * self.__height
