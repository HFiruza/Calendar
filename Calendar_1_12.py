import calendar
from calendar import month


def display_calendar():
    year = int(input('Введите год: '))
    month = int(input('Введите месяц (1-12): '))

    ca1 = calendar.TextCalendar(calendar.MONDAY)

    month_calendar = ca1.formatmonth(year, month)
    print(month_calendar)

display_calendar()