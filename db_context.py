from sqlalchemy import create_engine, Integer, Column, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import os

basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, '..statistic.db'), connect_args={'check_same_thread': False})
session = Session(bind=engine)

Base = declarative_base()


class DayStatistic(Base):
    __tablename__ = 'day statistic of visits'
    id = Column(Integer(), primary_key=True)
    unique_visitors = Column(Integer())
    visits = Column(Integer())
    date = Column(Date())


class MonthStatistic(Base):
    __tablename__ = 'month statistic of visits'
    id = Column(Integer(), primary_key=True)
    unique_visitors = Column(Integer())
    month = Column(String)
    visits = Column(Integer())


class YearsStatistic(Base):
    __tablename__ = 'years statistic of visits'
    id = Column(Integer(), primary_key=True)
    unique_visitors = Column(Integer())
    year = Column(String)
    visits = Column(Integer())


Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)