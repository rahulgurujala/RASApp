from dateutil.parser import parse
from pydantic import BaseModel, validator
from werkzeug.security import generate_password_hash


class UserRegisterSchema(BaseModel):
    username: str
    email: str
    password: str
    is_pro: bool = False
    profile_picture: str = None
    date_of_birth: str = None
    phone_number: str = None
    address: str = None

    class Config:
        orm_mode = True

    @validator("date_of_birth")
    def parse_date_of_birth(cls, v):
        return None if v is None else parse(v).date()

    @validator("password")
    def hash_password(cls, v):
        return generate_password_hash(v)


class LogIn(BaseModel):
    username: str
    password: str
