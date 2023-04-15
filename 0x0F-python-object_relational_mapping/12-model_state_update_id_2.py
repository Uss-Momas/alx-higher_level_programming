#!/usr/bin/python3
"""
Performing update to a state
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3])
                           )
    Session = sessionmaker(bind=engine)
    session = Session()
    # METHOD 1
    # result = session.query(State).filter_by(id=2).first() # filter 1
    # filter 2
    result = session.query(State).get(2)
    result.name = "New Mexico"
    session.add(result)
    session.commit()
    print(result.name)

    # METHOD 2
    # state = session.query(State).filter_by(id=2).update({'name': 'Arizona'})
    # print(state) # returns 1 for succes 0 for failure
    # print(result.name)
    # session.commit()
