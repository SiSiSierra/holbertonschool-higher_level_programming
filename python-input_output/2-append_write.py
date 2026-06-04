#!/usr/bin/python3
""" Module

Functions:
    append_write(filename, text)
"""


def append_write(filename="", text=""):
    """Append text to the end of a file

    Parameters:
        filename: Relative directory of file
        text: String to append to file
    """
    num = 0
    with open(filename, "a") as file:
        num = file.write(text)
    return num
