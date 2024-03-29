#!/usr/bin/python3
"""Prints the first state object from database
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(argv[1], argv[2], argv[3])
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    # will return a State object
    result = session.query(State).first()
    if result is None:
        print('Nothing')
    else:
        print("{}: {}".format(result.id, result.name))
