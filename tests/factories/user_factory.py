import factory

from db.models import User

from ..session import session


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = session

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    is_pro = False
    profile_picture = None
    date_of_birth = factory.Faker("date_of_birth")
    phone_number = None
    address = None
