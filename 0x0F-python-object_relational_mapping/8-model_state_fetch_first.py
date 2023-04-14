#!/usr/bin/python3
"""Prints the first state object from database
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(argv[1], argv[2], argv[3])
            )
    results = engine.execute("SELECT * FROM states")
    id, name = results.fetchone()
    print('{}: {}'.format(id, name))
