#!/usr/bin/python3
"""
Script that lists all states objects and corresponding City Objects
"""

from relationship_state import Base, State
from relationship_city import City
from sys import argv
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3])
                           )
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State, City).join(State).order_by(
            State.id.asc(), City.id.asc()
            )
    table = results.all()
    states = []
    for state, city in table:
        if state not in states:
            states.append(state)

    for state in states:
        print('{}: {}'.format(state.id, state.name))
        for st, city in table:
            if city.state_id == state.id:
                print('\t{}: {}'.format(city.id, city.name))

    session.close()
