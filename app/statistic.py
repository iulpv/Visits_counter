from collections import defaultdict

from app.db_context import DbContext, Visits


class VisitsStatistic:
    def day_statistic(self):
        unique_visitors, all_visitors = self._load_db_data()
        days = defaultdict(list)
        for el in unique_visitors:
            days[str(el[1])] = [len(list(filter(lambda item: item[1] == el[1], unique_visitors))),
                                len(list(filter(lambda item: item[1] == el[1], all_visitors)))
                                ]

        return days

    def month_statistic(self):
        unique_visitors, all_visitors = self._load_db_data()
        months = defaultdict(list)
        for el in unique_visitors:
            months[str(el[1].month)] = [len(list(filter(lambda item: item[1].month == el[1].month, unique_visitors))),
                                        len(list(filter(lambda item: item[1].month == el[1].month, all_visitors)))
                                        ]

        return months

    def year_statistic(self):
        unique_visitors, all_visitors = self._load_db_data()
        years = defaultdict(list)
        for el in unique_visitors:
            years[str(el[1].year)] = [len(list(filter(lambda item: item[1].year == el[1].year, unique_visitors))),
                                      len(list(filter(lambda item: item[1].year == el[1].year, all_visitors)))
                                      ]
        return years

    def _load_db_data(self):
        with DbContext() as session:
            unique_visitors = session.query(Visits.ip, Visits.date).distinct().all()
            all_visitors = session.query(Visits.ip, Visits.date).all()
        return unique_visitors, all_visitors
