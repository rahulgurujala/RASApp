from typing import Optional
from datetime import date
from dateutil.parser import parse
from pydantic import BaseModel, validator


class UserRegisterSchema(BaseModel):
    username: str
    email: str
    password: str
    is_pro: bool = False
    profile_picture: str = None
    date_of_birth: str = None
    phone_number: str = None
    address: str = None

    @validator("date_of_birth")
    def parse_date_of_birth(cls, v):
        return None if v is None else parse(v).date()
