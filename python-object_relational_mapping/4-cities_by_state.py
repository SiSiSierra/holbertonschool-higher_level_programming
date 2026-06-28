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
    cursor.execute("SELECT cities.id, cities.name, states.name \
FROM cities \
LEFT JOIN states ON cities.state_id = states.id \
ORDER BY id;")
    m = cursor.fetchall()
    for state in m:
        print(state)
    db.close()


if __name__ == "__main__":
    main()
