import factory

from db.models import Favourite

from ..session import session
from .image_factory import ImageFactory
from .user_factory import UserFactory


class FavouriteFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Favourite
        sqlalchemy_session = session

    user = factory.SubFactory(UserFactory)
    image = factory.SubFactory(ImageFactory)
