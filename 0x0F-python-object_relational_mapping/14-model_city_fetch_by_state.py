#!/usr/bin/python3
"""
Script that prints all cities from database table cities
"""

from sys import argv
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3])
                           )
    Session = sessionmaker(bind=engine)
    session = Session()
    # METHOD 1
    results = session.query(City, State).filter(City.state_id == State.id)
    for city, state in results.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    # METHOD 2 with  the join()
    # results = session.query(City).join(State)
    # print(results)
