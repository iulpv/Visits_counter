def formation_stat(days_query, months_query, years_query):
    days_stat = {"статистика по дням": []}
    months_stat = {"статистика по месяцам": []}
    years_stat = {"статистика по годам": []}
    for day in days_query:
        days_stat["статистика по дням"].append(
            {
                str(day.date): [
                    {"уникальные пользователи": day.unique_visitors},
                    {"все пользователи": day.visits}
                ]
            }
        )
        #months_visits[day.date.month] += day.visits

    for month in months_query:
        months_stat["статистика по месяцам"].append(
            {
                str(month.month): [
                    {"пользователи": month.visits},
                    {"уникальные пользователи": month.unique_visitors}
                ]
            }
        )
        #year_visits[month.date.year] += months_visits

    for year in years_query:
        years_stat["статистика по годам"].append(
            {
                str(year.year): [
                    {"все пользователи": year.visits},
                    {"уникальные пользователи": year.unique_visitors}
                ]
            }
        )
    return {"Statistic": [days_stat, months_stat, years_stat]}
