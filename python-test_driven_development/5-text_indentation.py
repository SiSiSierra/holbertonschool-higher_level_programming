#!/usr/bin/python3
"""Module with helper functions

Functions:
    text_indentation(text): Print text with indents after some\
    special characters

"""


def text_indentation(text):
    """ Print given text with 2 new lines \
    after occurances of '?', ':', '.'

    Parameters:
        text: String to parse

    Returns: nothing
    """
    newline = False
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in text:
        if i == ' ' and newLine is True:
            continue
        elif i not in ['.', '?', ':']:
            newLine = False
            print(i, end="")
        else:
            newLine = True
            print(f"{i}\n\n", end="")
