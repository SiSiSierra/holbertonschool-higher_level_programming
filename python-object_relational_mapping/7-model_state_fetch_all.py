#!/usr/bin/python3
"""Module to list all states from db
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    conn = engine.connect()
    result = conn.execute(select([State]).order_by("id"))
    i = 0
    for row in result:
        i += 1
        print("{}: {}".format(i, row[1]))
