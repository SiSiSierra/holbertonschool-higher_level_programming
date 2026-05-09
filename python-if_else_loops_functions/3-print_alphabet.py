#!/usr/bin/python3
for i in range(26):
    if i == 4 or i == 16:
        continue
    print("{0:c}".format(i + 97), end='')
