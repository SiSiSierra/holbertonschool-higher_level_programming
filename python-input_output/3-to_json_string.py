#!/usr/bin/python3
"""Module

Functions:
    to_json_string(my_obj)
"""
import json


def to_json_string(my_obj):
    """Convert object to JSON string

    Parameters:
        my_obj: Any object

    Returns: JSON string version of object
    """
    return json.dumps(my_obj)
