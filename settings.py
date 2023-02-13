from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = ConfigParser()
config.read('config.ini')

class Settings():
    connection_string = config.get('mysql', 'connection_string')

    @classmethod
    def create_session(cls):
        engine = create_engine(cls.connection_string)
        Session = sessionmaker(bind=engine)
        try:
            yield Session()
        finally:
            Session().close()


session = Settings.create_session