#!/usr/bin/python3
""" Module

Functions:
    inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """Determines if obj inherits from a_class

    Parameters:
        obj: Object to test
        a_class: Class to compare to

    Returns: True or false depending if signatures match
    """
    return issubclass(type(obj), a_class) and not (type(obj) is a_class)
