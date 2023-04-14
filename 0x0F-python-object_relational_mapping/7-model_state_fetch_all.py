#!/usr/bin/python3
"""Listing all states from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    engine = create_engine(
                "mysql+mysqldb://{}:{}@localhost:3306/{}"
                .format(username, passwd, db_name)
            )
    results = engine.execute("SELECT * from states")
    rows = dict(results.fetchall())
    for key, value in rows.items():
        print('{}: {}'.format(key, value))
