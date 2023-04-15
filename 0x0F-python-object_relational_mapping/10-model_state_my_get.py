#!/usr/bin/python3
"""
Print the state object in the database with the name passed as argument
"""

from sys import argv, exit
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3])
                           )
    # mode 1
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = argv[4]
    state = session.query(State).filter_by(name=state_name).first()
    if state is None:
        print('Not found')
        exit(1)
    print(state.id)

    # mode 2
    # with engine.connect() as conn:
    #    filter = text("""SELECT * FROM states WHERE name LIKE :name""")
    #    result = conn.execute(filter, name=argv[4]).fetchone()
    #    print(result[0])
