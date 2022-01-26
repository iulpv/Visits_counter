from sqlalchemy import create_engine, Integer, Column, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import os

Base = declarative_base()


class DbContext:
    def __init__(self):
        self.session = None

    def __enter__(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        engine = create_engine('sqlite:///' + os.path.join(basedir, '../statistic.db'),
                               connect_args={'check_same_thread': False})
        self.session = Session(bind=engine)
        Base.metadata.create_all(engine)
        # Base.metadata.drop_all(engine)
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.commit()
        self.session.close()


class Visits(Base):
    __tablename__ = 'visits'
    id = Column(Integer(), primary_key=True)
    ip = Column(String())
    date = Column(Date())
