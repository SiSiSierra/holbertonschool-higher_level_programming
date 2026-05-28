#!/usr/bin/python3
"""Module with lookup function

Functions:
    lookup(obj)

"""


def lookup(obj):
    """Returns the class functions and attributes in obj

    Parameters:
        obj: obj to lookup

    Returns: All names in obj
    """
    return (dir(obj))
