#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    c = 0
    C = 0
    for i in range(0, len(new_string)):
        if new_string[i] == 'c':
            c += 1
        elif new_string[i] == "C":
            C += 1
    for i in range(0, c):
        new_string.remove("c")
    for i in range(0, C):
        new_string.remove("C")
    return "".join(new_string)
