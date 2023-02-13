from sqlalchemy import Column, Date, ForeignKey, String, Text, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship

from .base import BaseModel


class User(BaseModel):
    __tablename__ = "Users"

    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    is_pro = Column(TINYINT(1), server_default=text("0"))
    profile_picture = Column(Text)
    date_of_birth = Column(Date)
    phone_number = Column(String(20))
    address = Column(Text)


class Device(BaseModel):
    __tablename__ = "Devices"

    user_id = Column(ForeignKey("Users.id"), nullable=False, index=True)
    device_name = Column(String(255), nullable=False)
    device_type = Column(String(255), nullable=False)

    user = relationship("User")


class Image(BaseModel):
    __tablename__ = "Images"

    user_id = Column(
        ForeignKey("Users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    text = Column(Text, nullable=False)
    image_url = Column(Text, nullable=False)

    user = relationship("User")


class Favourite(BaseModel):
    __tablename__ = "Favourites"

    user_id = Column(
        ForeignKey("Users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    image_id = Column(
        ForeignKey("Images.id", ondelete="CASCADE"), nullable=False, index=True
    )

    image = relationship("Image")
    user = relationship("User")
