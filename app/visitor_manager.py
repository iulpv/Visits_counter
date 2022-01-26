import datetime
from app.statistic import VisitsStatistic
from app.db_context import DbContext, Visits


class VisitorManager:
    def __init__(self):
        self.visits_statistic_manager = VisitsStatistic()

    def handle_visitor(self, ip):
        date = datetime.datetime.now().date()
        with DbContext() as session:
            visit = Visits(ip=ip, date=date)
            session.add(visit)

    def take_statistic(self, by_day=False, by_month=False, by_year=False):
        if by_day:
            return self.visits_statistic_manager.day_statistic()
        elif by_month:
            return self.visits_statistic_manager.month_statistic()
        elif by_year:
            return self.visits_statistic_manager.year_statistic()
