#!/usr/bin/python3
""" Module that defines a class

Classes:
    Square(): Defines a square class
"""


class Square():
    """ Square class

    Attributes:
        private __size: Size of width and height

    Functions:
        public area(): Return area of square

    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
