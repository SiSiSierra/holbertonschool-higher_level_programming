#!/usr/bin/python3
""" Module

Functions:
    read_file(filename="")
"""


def read_file(filename=""):
    """Read a file and print the contents

    Paramaters:
        filename: Relative directory to file
    """
    with open(filename, "r") as file:
        content = file.read()
        print(content, end="")
