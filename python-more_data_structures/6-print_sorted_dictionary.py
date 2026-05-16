#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keylist = []
    for i in a_dictionary.keys():
        keylist.append(i)
    keylist.sort()
    for i in keylist:
        print("{0}: {1}".format(i, a_dictionary[i]))
