#!/usr/bin/python3
""" Module that defines a class

Classes:
    Square(): Defines a square class
"""


class Square():
    """ Square class

    Attributes:
        __size: Size of width and height
        __position: Tuple of 2 ints for offset

    Functions:
        area(): Return area of square
        my_print(): Print the square as hashes
    """
    def __init__(self, size=0, position=(0, 0)):
        """Intialises the Square class with size and position

        Parameters:
            size: Int indicating width on all sides
            position: Tuple of ints indicating offset in stdout

        Returns: The new square object
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Gets the size attribute

        Returns: __size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Sets the size attribute with an integer

        Returns: nothing
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Gets the position attribute

        Returns: __position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Sets the position attribute with a given tuple

        Returns: nothing
        """
        if type(value) is not tuple or len(value) < 2\
            or type(value[0]) is not int or type(value[1]) is not int\
                or min(value) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculates the area of the square

        Returns: size squared
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Prints the square with # characters

        Returns: nothing
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[0]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[1]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
