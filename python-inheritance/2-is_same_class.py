#!/usr/bin/python3
""" Module

Functions:
    is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """Determines if obj is an instance of a_class

    Parameters:
        obj: Object to test
        a_class: Class to compare to

    Returns: True or false depending if signatures match
    """
    return type(obj) is a_class
