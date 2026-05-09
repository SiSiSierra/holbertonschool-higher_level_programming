#!/usr/bin/python3
def pow(a, b):
    j = a
    if b < 0:
        b *= -1
        a = 1
        for i in range(b):
            a = a / j
    else:
        for i in range(b - 1):
            a *= j
    return a
