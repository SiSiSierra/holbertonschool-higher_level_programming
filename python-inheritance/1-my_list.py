#!/usr/bin/python3
"""Module

Classes:
    MyList

"""


class MyList(list):
    """MyList

    Functions:
        print_sorted(self): print list as if it was sorted
    """
    def print_sorted(self):
        copy = self.copy()
        copy.sort()
        print(copy)
        del copy
