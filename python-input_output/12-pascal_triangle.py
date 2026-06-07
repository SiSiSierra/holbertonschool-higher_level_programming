#!/usr/bin/python3
"""Module

Functions:
    pascal_triangle(n)
"""


def pascal_triangle(n):
    """ Make a list of given row in pascals triangle

    Params:
        n: Row of pascal's triangle to find (n>=0)

    Returns: ordered list of ints based on pascals triangle
    """

    tri = []
    if n <= 0:
        return []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(combination(i, j))
        tri.append(row)
    return tri


def factorial(n):
    if n == 0:
        return 1
    i = n
    for j in range(n-1):
        i = i * (n - 1)
        n -= 1
    return i


def combination(n, k):
    a = factorial(n)
    b = factorial(k)
    c = factorial(n-k)
    d = b * c
    return a // d
