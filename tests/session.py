from sqlalchemy.orm import sessionmaker


def Session():
    session = sessionmaker()
    return session()


session = Session()
