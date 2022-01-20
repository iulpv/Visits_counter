import datetime
from db_context import session, DayStatistic, MonthStatistic, YearsStatistic
from statistic import formation_stat


def update_statistic(unique_day=False, unique_month=False, unique_year=False):
    date = datetime.datetime.now().date()
    query = session.query(DayStatistic).filter(
        DayStatistic.date == date).first()
    if query is None:
        entry = DayStatistic(date=date, visits=1, unique_visitors=1 if unique_day else 0)
        session.add(entry)
    else:
        query.visits += 1
        if unique_day:
            query.unique_visitors += 1

    month = datetime.datetime.now().month
    query = session.query(MonthStatistic).filter(
        MonthStatistic.month == str(month)).first()
    if query is None:
        entry = MonthStatistic(month=str(month), visits=1, unique_visitors=1 if unique_month else 0)
        session.add(entry)
    else:
        query.visits += 1
        if unique_month:
            query.unique_visitors += 1

    year = datetime.datetime.now().year
    query = session.query(YearsStatistic).filter(
        YearsStatistic.year == str(year)).first()
    if query is None:
        entry = YearsStatistic(year=str(year), visits=1, unique_visitors=1 if unique_year else 0)
        session.add(entry)
    else:
        query.visits += 1
        if unique_year:
            query.unique_visitors += 1

    session.commit()


def take_statistic():
    query_day = session.query(DayStatistic)
    query_month = session.query(MonthStatistic)
    query_year = session.query(YearsStatistic)
    return formation_stat(query_day, query_month, query_year)
