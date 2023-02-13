from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


class CRUD:
    @classmethod
    def add(cls, session: Session, obj: object):
        session.add(obj)
        session.commit()
        return obj

    @classmethod
    def get_by_id(cls, session: Session, _id: int):
        return session.query(cls).get(_id)

    @classmethod
    def get_all(cls, session: Session):
        return session.query(cls).all()

    @classmethod
    def create_or_fail(cls, session: Session, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            return None
        return obj

    @classmethod
    def update(cls, session: Session, _id: int, **kwargs):
        obj = session.query(cls).get(_id)
        if not obj:
            return None
        for attr, value in kwargs.items():
            setattr(obj, attr, value)
        session.commit()
        return obj

    @classmethod
    def filter(cls, session: Session, **kwargs):
        return session.query(cls).filter_by(**kwargs)

    @classmethod
    def join(cls, session: Session, join_table, join_on):
        return session.query(cls).join(join_table, join_on)
