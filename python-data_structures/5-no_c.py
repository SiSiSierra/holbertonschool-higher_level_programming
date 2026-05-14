#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    for i in range(0, len(new_string)):
        if new_string[i] == 'c' or new_string[i] == "C":
            new_string.pop(i)
            return "".join(new_string)
