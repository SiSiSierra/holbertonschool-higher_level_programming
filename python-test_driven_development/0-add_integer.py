#!/usr/bin/python3
""" Module containing helper functions

Functions:
    add_integer(a, b)
"""
def add_integer(a, b=98):
    """ Adds integers a and b together

    Parameters:
        a: First int to add
        b: Second int to add

    Returns:
        Sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
