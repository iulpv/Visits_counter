import datetime
from collections import defaultdict
from sqlalchemy import select, funcfilter
from app.db_context import DbContext, Visits
from sqlalchemy.sql import extract


class VisitsStatistic:
    def day_statistic(self):
        day_filter = lambda x: Visits.date == x[0]
        f = lambda y: y
        return self.stat(day_filter, f)

    def month_statistic(self):
        month_filter = lambda x: extract('month', Visits.date) == x[0].month
        f = lambda y: y.month
        return self.stat(month_filter, f)

    def year_statistic(self):
        year_filter = lambda x: extract('year', Visits.date) == x[0].year
        f = lambda y: y.year
        return self.stat(year_filter, f)

    def stat(self, my_filter, for_date):
        stat = dict()
        with DbContext() as session:
            for date in self.take_db_dates():
                response_all = session.query(Visits.ip).filter(my_filter(date)).count()
                response_unique = session.query(Visits.ip).filter(my_filter(date)).distinct().count()
                stat[str(for_date(date[0]))] = ['все пользователи:' + str(response_all),
                                                'уникальные:' + str(response_unique)]

        return stat

    def take_db_dates(self):
        with DbContext() as session:
            return session.query(Visits.date).distinct().all()
