#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from model_city import City

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    # generate database schema
    Base.metadata.create_all(engine)

    # SQLAlchemy ORM session factory bound to this engine
    Session = sessionmaker(bind=engine)
    # Create a new session
    session = Session()

    # Create, add and commit new object to DB.
    result = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()

    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
