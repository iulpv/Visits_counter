import datetime
import random
from db_operations import update_statistic


class VisitorManager:
    def __init__(self):
        self.unique_day_visitors = set()
        self.unique_month_visitors = set()
        self.unique_year_visitors = set()

    def handle_visitor(self, ip):
        ip = self.magic_ip(ip)
        unique_day_visitor, unique_month_visitor, unique_year_visitor = self.define_new_visitor(ip)
        update_statistic(unique_day_visitor, unique_month_visitor, unique_year_visitor)


    def magic_ip(self, ip):
        if random.randint(1, 2) == 2:
            return ".".join(map(str, (random.randint(0, 255)
                                      for _ in range(4))))
        return ip

    def define_new_visitor(self, ip):
        self.clear_old_visitors()
        unique_day_visitor = (ip, datetime.datetime.now().date()) not in self.unique_day_visitors
        self.unique_day_visitors.add((ip, datetime.datetime.now().date()))
        unique_month_visitor = (ip, datetime.datetime.now().month) not in self.unique_month_visitors
        self.unique_month_visitors.add((ip, datetime.datetime.now().month))
        unique_year_visitor = (ip, datetime.datetime.now().year) not in self.unique_year_visitors
        self.unique_year_visitors.add((ip, datetime.datetime.now().year))

        return unique_day_visitor, unique_month_visitor, unique_year_visitor

    def clear_old_visitors(self):
        for visitor in self.unique_day_visitors:
            if visitor[1] != datetime.datetime.now().date():
                self.unique_day_visitors.remove(visitor)

        for visitor in self.unique_month_visitors:
            if visitor[1] != datetime.datetime.now().month:
                self.unique_month_visitors.remove(visitor)
