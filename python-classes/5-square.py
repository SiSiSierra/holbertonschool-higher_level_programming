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
        public my_print(): Print the square as hashes
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
