import datetime
from db_context import session, DayStatistic, MonthStatistic, YearsStatistic
from visitors import VisitorManager
from db_operations import update_statistic


def test_day_visits():
    update_statistic()
    query = session.query(DayStatistic).filter(
        DayStatistic.date == datetime.datetime.now().date()).first()
    vis = query.visits
    manager = VisitorManager()
    ip = '0.0.0.0'
    manager.handle_visitor(ip)
    assert query.visits != vis


def test_month_visits():
    update_statistic()
    month = datetime.datetime.now().month
    query = session.query(MonthStatistic).filter(
        MonthStatistic.month == str(month)).first()
    vis = query.visits
    manager = VisitorManager()
    ip = '0.0.0.0'
    manager.handle_visitor(ip)
    assert query.visits != vis


def test_year_visits():
    update_statistic()
    year = datetime.datetime.now().year
    query = session.query(YearsStatistic).filter(
        YearsStatistic.year == str(year)).first()
    vis = query.visits
    manager = VisitorManager()
    ip = '0.0.0.0'
    manager.handle_visitor(ip)
    assert query.visits != vis


def test_add_unique_visitors():
    manager = VisitorManager()
    ip = '0.0.0.0'
    manager.handle_visitor(ip)
    assert len(manager.unique_day_visitors) != 0


def test_del_last_day_visitors():
    manager = VisitorManager()
    manager.unique_day_visitors.add(("0.0.0.0", datetime.datetime(2022, 1, 24)))
    a = ("0.0.0.0", datetime.datetime(2022, 1, 24)) in manager.unique_day_visitors
    manager.clear_old_visitors()
    b = ("0.0.0.0", datetime.datetime(2022, 1, 24)) in manager.unique_day_visitors
    assert a != b


