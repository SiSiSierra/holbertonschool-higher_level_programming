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
    cursor.execute("SELECT * FROM states WHERE name COLLATE utf8mb4_bin \
LIKE \'N%\' ORDER BY id;")
    m = cursor.fetchall()
    for state in m:
        print(state)
    db.close()


if __name__ == "__main__":
    main()
