#!/usr/bin/python3
def pow(a, b):
    j = a
    for i in range(b - 1):
        a *= j
    return a
