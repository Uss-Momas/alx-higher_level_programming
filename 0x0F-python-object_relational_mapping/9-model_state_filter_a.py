#!/usr/bin/python3
"""
Listing all states that contain the letter 'a' in it
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine, text)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3])
                           )
    # MODE 1
    sql_text = text(
            "SELECT * FROM states WHERE name LIKE '%a%' ORDER BY id ASC"
            )
    result = engine.execute(sql_text)
    table = result.fetchall()
    for state_id, state_name in table:
        print('{}: {}'.format(state_id, state_name))

    # MODE 2 - Creating states object
    # Session = sessionmaker(bind=engine)
    # session = Session()
    # objects = session.query(State).filter(State.name.like('%a%')).all()
    # for obj in objects:
    #    print('{}: {}'.format(obj.id, obj.name))
