#!/usr/bin/python3
"""Script to list all cities from db
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.name, City.id, City.name)\
            .select_from(City).join(State, City.state_id == State.id)\
            .order_by(City.id)
    for row in result:
        print(f"{row[0]}: ({row[1]}) {row[2]}")
