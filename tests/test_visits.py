import datetime
import pytest
from app.visitor_manager import VisitorManager
from app.db_context import DbContext, Visits
from app import check_ip


def test_add_bd():
    v = VisitorManager()
    ip = '1.1.1.1'
    v.handle_visitor(ip)
    with DbContext() as session:
        date = datetime.datetime(2022, 1, 26)
        visit = session.query(Visits).filter(Visits.ip == ip, Visits.date == date.date()).first()
        assert visit is not None
        session.delete(visit)


def test_day_visits():
    v = VisitorManager()
    stat = v.take_statistic(by_day=True)
    ip = '1.1.1.1'
    date = datetime.datetime(2022, 1, 26).date()
    v.handle_visitor(ip)
    stat2 = v.take_statistic(by_day=True)
    assert stat[str(date)] != stat2[str(date)]


def test_month_visits():
    v = VisitorManager()
    stat = v.take_statistic(by_month=True)
    ip = '1.1.1.1'
    date = datetime.datetime(2022, 1, 26).date().month
    v.handle_visitor(ip)
    stat2 = v.take_statistic(by_month=True)
    assert stat[str(date)] != stat2[str(date)]


def test_year_visits():
    v = VisitorManager()
    stat = v.take_statistic(by_year=True)
    ip = '1.1.1.1'
    date = datetime.datetime(2022, 1, 26).date().year
    v.handle_visitor(ip)
    stat2 = v.take_statistic(by_year=True)
    assert stat[str(date)] != stat2[str(date)]


def test_check_ip():
    ip = check_ip('12234.2.1.')
    assert ip != True
