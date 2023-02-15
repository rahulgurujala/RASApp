from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

config = ConfigParser()
config.read("config.ini")


# TODO: Need to Refactor
class Settings:
    connection_string = config.get("mysql", "connection_string")
    SECRET_KEY = config.get("secret", "secret_key")
    bucket_name = config.get("aws", "bucket_name")
    aws_access_key_id = config.get("aws", "aws_access_key_id")
    aws_secret_access_key = config.get("aws", "aws_secret_access_key")

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
aws = Settings
