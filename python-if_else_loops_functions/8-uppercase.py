#!/usr/bin/python3
def uppercase(str):
    for i in str:
        offset = 0
        if 97 <= ord(i) <= 122:
            offset = 32
        print("{0:c}".format(ord(i) - offset ), end='')
    print('')
