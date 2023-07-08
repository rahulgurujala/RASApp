from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Query, Session


class crud:
    """A CRUD utility class for SQLAlchemy models."""

    @classmethod
    def create(cls, session: Session, **kwargs: dict) -> object:
        """
        Create a new object in the database.

        Parameters:
        -----------
        session: sqlalchemy.orm.Session
            The session to use for database operations.
        **kwargs:
            The new values to update the object with.

        Returns:
        --------
        object
            The created object with its primary key set.
        """
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()
        return obj

    @classmethod
    def get_by_id(cls, session: Session, _id: int) -> object:
        """
        Retrieve an object from the database by ID.

        Parameters:
        -----------
        session: sqlalchemy.orm.Session
            The session to use for database operations.
        _id: int
            The ID of the object to retrieve from the database.

        Returns:
        --------
        object
            The retrieved object, or None if not found.
        """
        return session.query(cls).get(_id)

    @classmethod
    def filter(cls, session: Session, *args) -> Query:
        """
        Filter objects from the database by criterion.

        Parameters:
        -----------
        session: sqlalchemy.orm.Session
            The session to use for database operations.
        *criterion:
            A list of criteria to use for filtering the objects.

        Returns:
        --------
        list
            A list of the filtered objects.
        """
        return session.query(cls).filter(*args)

    @classmethod
    def filter_by(cls, session: Session, **kwargs) -> List[object]:
        """
        Filter objects from the database by keyword arguments.

        Parameters:
        -----------
        session: sqlalchemy.orm.Session
            The session to use for database operations.
        **kwargs:
            The keyword arguments to use for filtering the objects.

        Returns:
        --------
        list
            A list of the filtered objects.
        """
        return session.query(cls).filter_by(**kwargs).all()

    @classmethod
    def update(cls, session: Session, obj: object, **kwargs) -> object:
        """
        Update an object in the database with new values.

        Parameters:
        -----------
        session: sqlalchemy.orm.Session
            The session to use for database operations.
        obj: object
            The object to be updated in the database.
        **kwargs:
            The new values to update the object with.

        Returns:
        --------
        object
            The updated object.
        """
        for attr, value in kwargs.items():
            setattr(obj, attr, value)
        session.commit()
        return obj

    @classmethod
    def first(cls, session: Session, *agrs) -> object:
        """
        Returns the first element that matches the filter criteria, or None if no such element exists.

        Parameters:
        -----------
        session: sqlalchemy.orm.Session
            The session to use for database operations.
        args:
            positional filter arguments to pass to the filter method.

        Returns:
        --------
            The updated object. the first matching object, or None if no match is found.
        """
        return session.query(cls).filter(*agrs).first()

    @classmethod
    def get_by(cls, session: Session, **kwargs) -> object:
        """
        Returns the first object that matches the filter criteria, or None if no such object exists.

        Parameters:
        -----------
        session: sqlalchemy.orm.Session
            The session to use for database operations.
        **kwargs:
            keyword arguments to pass to the filter_by method.

        Returns:
        --------
            the first matching object, or None if no match is found.
        """
        return session.query(cls).filter_by(**kwargs).first()

    def create_or_fail(self, session: Session, obj: object) -> object:
        """
        Attempt to add the given object to the database, but fail and rollback the transaction if there is a unique
        constraint violation.

        Parameters:
        -----------
        session: sqlalchemy.orm.Session
            The session to use for database operations.
        obj:
            the object to add to the database.

        Returns:
        --------
            the added object, or None if a unique constraint violation occurred.
        """
        try:
            session.add(obj)
            session.commit()
            return obj
        except IntegrityError:
            session.rollback()
            return None
