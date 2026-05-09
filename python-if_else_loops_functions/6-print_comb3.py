#!/usr/bin/python3
for i in range(9):
    for j in range(9 - i):
        if i < 8:
            print("{0:02d}".format(11 * i + j + 1), end=', ')
        else:
            print("{0:02d}".format(11 * i + j + 1))
