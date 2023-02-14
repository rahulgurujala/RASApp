from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


class CRUD:
    @classmethod
    def create(cls, session: Session, obj: object):
        session.add(obj)
        session.commit()
        return obj

    @classmethod
    def get_by_id(cls, session: Session, _id: int):
        return session.query(cls).get(_id)

    @classmethod
    def filter(cls, session: Session, **kwargs):
        return session.query(cls).filter_by(**kwargs).all()

    @classmethod
    def update(cls, session: Session, obj: object, **kwargs):
        for attr, value in kwargs.items():
            setattr(obj, attr, value)
        session.commit()
        return obj

    @classmethod
    def join(cls, session: Session, *args):
        return session.query(cls).join(*args)

    @classmethod
    def get_all(cls, session: Session):
        return session.query(cls).all()

    @classmethod
    def get(cls, session: Session, **kwargs):
        return session.query(cls).filter_by(**kwargs).first()

    @classmethod
    def create_or_fail(cls, session: Session, obj: object):
        try:
            session.add(obj)
            session.commit()
            return obj
        except IntegrityError:
            session.rollback()
            return None
