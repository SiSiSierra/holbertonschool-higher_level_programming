from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimeter(self):
        ...


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return abs(self.__radius**2 * math.pi)

    def perimeter(self):
        return abs(self.__radius * math.pi * 2)


class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return self.__width * 2 + self.__height * 2


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
