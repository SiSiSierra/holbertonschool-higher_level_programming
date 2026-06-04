#!/usr/bin/python3
"""Module

Functions:
    load_from_json_file(filename)
"""
import json


def load_from_json_file(filename):
    """Create object from data in JSON file

    Parameters:
        filename: FIle to load

    Returns: Loaded object
    """
    with open(filename, "r") as file:
        thing = json.loads(file.read())
    return thing
