#!/usr/bin/python3
"""
Listing all cities objects
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3])
                           )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    table = session.query(State).all()
    for state in table:
        for city in state.cities:
            print('{}: {} -> {}'.format(city.id, city.name, state.name))
    session.close()
