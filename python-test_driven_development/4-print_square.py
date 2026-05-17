#!/usr/bin/python3
"""Module to print a square

Functions:
    print_square(size): Print a hash square of given size

"""


def print_square(size):
    """Print a square of hashes (#)

    Parameters:
        size: Height and width of square

    Returns:
        nothing
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
