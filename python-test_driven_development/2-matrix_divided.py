#!/usr/bin/python3
""" Module of helper functions

Functions:
    matrix_divided(matrix, div): Multiply elements of matrix by div

"""


def matrix_divided(matrix, div):
    """ Divides every element in a matrix by div

    Paramters:
        matrix: List of lists of integers or floats
        div: Number to divide by

    Returns:
        New matrix of results of divisions
    """

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    new = []
    try:
        length = len(matrix[0])
    except IndexError:
        return (new)
    for i in matrix:
        app = []
        if len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            app.append(round(j / div, 2))
        new.append(app)
    return (new)
