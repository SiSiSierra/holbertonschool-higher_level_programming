#!/usr/bin/python3
import sys
def main():
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {0}".format(sys.argv[1]))
    else:
        print("{0} arguments:".format(len(sys.argv) - 1))
        j = 0
        for i in sys.argv:
            if j > 0:
                print("{0}: {1}".format(j, sys.argv[j]))
            j = j + 1


if __name__ == "__main__":
    main()
