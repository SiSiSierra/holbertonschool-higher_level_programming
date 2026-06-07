#!/usr/bin/python3
"""Module

Functions:
    class_to_json(obj)
"""


def class_to_json(obj):
    """ Convert obj to dictionary

    Parameters:
        obj: Any object

    Returns: obj as dictionary
    """
    return (obj.__dict__)
