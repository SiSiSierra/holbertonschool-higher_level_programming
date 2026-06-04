#!/usr/bin/python3
""" Module

Functions:
    write_file(filename, text)
"""


def write_file(filename="", text=""):
    """Write some text to a file, overwriting the contents

    Parameters:
        filename: Relative file directory
        text: String to write
    """
    num = 0
    with open(filename, "w") as file:
        num = file.write(text)
    return num
