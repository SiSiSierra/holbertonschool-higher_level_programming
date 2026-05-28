#!/usr/bin/python3
""" Module

Functions:
    is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """Determines if obj is an instance of a_class

    Parameters:
        obj: Object to test
        a_class: Class to compare to

    Returns: True or false depending if signatures match
    """
    return isinstance(obj, a_class)
