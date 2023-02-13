import factory

from db.models import Image

from ..session import session
from .user_factory import UserFactory


class ImageFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Image
        sqlalchemy_session = session

    text = factory.Faker("text")
    image_url = factory.Faker("image_url")
    user = factory.SubFactory(UserFactory)
