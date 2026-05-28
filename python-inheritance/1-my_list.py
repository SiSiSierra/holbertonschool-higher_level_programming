#!/usr/bin/python3
"""Module

Classes:
    MyList

"""


class MyList(list):

    def print_sorted(self):
        copy = self.copy()
        copy.sort()
        print(copy)
        del copy
