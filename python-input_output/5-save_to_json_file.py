#!/usr/bin/python3
"""Module

Functions:
    save_to_json_file(my_obj, filename)
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file as JSON

    Parameters:
        my_obj: Object to save
        filename: File to save to
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
