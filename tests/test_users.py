from tests.factories.user_factory import UserFactory
from db.models import User


def test_user_device_association(db_session):
    user = UserFactory.create()
    # add the user to the database session
    db_session.add(user)
    # commit the changes to the database
    db_session.commit()
    # retrieve the user from the database
    user_from_db = db_session.query(User).get(user.id)
    # assert that the user is not None
    assert user_from_db is not None
    # assert that the attributes of the user match
    assert user.user_id == user_from_db.user_id
    assert user.image_id == user_from_db.image_id
