#!/usr/bin/python3
""" Module to test connecting to the local database

Functions
    main()
"""
import MySQLdb
import sys


def main():
    """ main program function
    """
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name \
FROM cities \
LEFT JOIN states \
ON cities.state_id = states.id \
WHERE BINARY states.name = (\"{}\")".format(sys.argv[4]))
    m = cursor.fetchall()
    comma = ""
    for city in m:
        print("{}{}".format(comma, city[0]), end="")
        comma = ", "
    print()
    db.close()


if __name__ == "__main__":
    main()
