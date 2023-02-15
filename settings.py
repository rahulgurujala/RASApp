from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

config = ConfigParser()
config.read("config.ini")


class Settings:
    connection_string = config.get("mysql", "connection_string")
    SECRET_KEY = config.get("secret", "secret_key")

    @classmethod
    def create_session(cls):
        engine = create_engine(cls.connection_string)
        Session = scoped_session(sessionmaker(bind=engine))
        try:
            yield Session()
        finally:
            Session().close()


session = Settings.create_session
SECRET_KEY = Settings.SECRET_KEY
