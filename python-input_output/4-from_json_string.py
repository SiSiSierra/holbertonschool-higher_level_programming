#!/usr/bin/python3
"""Module

Functions:
    from_json_string(my_str)
"""
import json


def from_json_string(my_str):
    """Load a JSON string into a python object

    Parameters:
        my_str: String to load into an object
    """
    return json.loads(my_str)
