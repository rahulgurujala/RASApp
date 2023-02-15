from tests.factories.favourite_factory import FavouriteFactory
from db.models import Favourite


def test_favourite_model(db_session):
    # create a favourite using the factory
    favourite = FavouriteFactory.create()
    # add the favourite to the database session
    db_session.add(favourite)
    # commit the changes to the database
    db_session.commit()
    # retrieve the favourite from the database
    favourite_from_db = db_session.query(Favourite).get(favourite.id)
    # assert that the favourite is not None
    assert favourite_from_db is not None
    # assert that the attributes of the favourite match
    assert favourite.user_id == favourite_from_db.user_id
    assert favourite.image_id == favourite_from_db.image_id
