#!/usr/bin/python3
def print_reversed_list_integer(mylist=[]):
    for i in range(0, len(mylist)):
        print("{:d}".format(mylist[len(mylist) - i - 1]))
