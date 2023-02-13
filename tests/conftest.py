import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import BaseModel


@pytest.fixture(scope="session")
def engine():
    return create_engine("sqlite:///test.db")


@pytest.fixture(scope="session")
def db_session(engine):
    # Create the test database tables
    BaseModel.metadata.create_all(engine)

    # Create a session for interacting with the test database
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session

    # Close the database session and remove all the data
    session.close()
    BaseModel.metadata.drop_all(engine)
