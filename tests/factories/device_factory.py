import factory

from db.models import Device

from ..session import session
from .user_factory import UserFactory


class DeviceFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Device
        sqlalchemy_session = session

    device_name = factory.Faker("device_name")
    device_type = factory.Faker("device_type")
    user = factory.SubFactory(UserFactory)
