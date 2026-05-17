#!/usr/bin/python3
"""Module with helper functions

Functions:
    say_my_name(first_name, last_name): Print out given strings together)
"""


def say_my_name(first_name, last_name=""):
    """Print out 'My name is ' followed by first and last name

    Parameters:
        first_name: First name as string
        last_name: Last name as string

    Returns:
        nothing
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
