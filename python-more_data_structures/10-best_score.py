#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)
    best = None
    for i in a_dictionary:
        if best == None or a_dictionary[i] > a_dictionary[best]:
            best = i
    return (best)
