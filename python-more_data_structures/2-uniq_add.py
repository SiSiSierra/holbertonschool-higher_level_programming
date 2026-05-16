#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    seen = []
    for i in my_list:
        if i not in seen:
            a += i
            seen.append(i)
    return (a)
