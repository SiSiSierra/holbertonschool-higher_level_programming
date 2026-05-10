#!/usr/bin/python3
import sys


def main():
    j = 0
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        j += int(sys.argv[i])
    print(j)


if __name__ == "__main__":
    main()
