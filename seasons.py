# -*- coding: utf-8 -*-
from datetime import date, datetime

SUMMER = 'Summer'
WINTER = 'Winter'
SPRING = 'Spring'
AUTUMN = 'Autumn'

_DUMMY_YEAR = 2000 # dummy leap year to allow input X-02-29 (leap day)

def _dummy_date(month, day):
    return date(_DUMMY_YEAR, month, day)

# Reference: https://stackoverflow.com/questions/16139306/determine-season-given-timestamp-in-python-using-datetime
def get_season(timestamp):
    if isinstance(timestamp, datetime):
        timestamp = timestamp.date()

    seasons_intervals = [
        (SUMMER, (_dummy_date(1,  1),  _dummy_date(2, 29))),
        (AUTUMN, (_dummy_date(3, 1),  _dummy_date(5, 31))),
        (WINTER, (_dummy_date(6, 1),  _dummy_date(8, 31))),
        (SPRING, (_dummy_date(9, 1),  _dummy_date(11, 30))),
        (SUMMER, (_dummy_date(12, 1),  _dummy_date(12, 31)))
    ]

    timestamp = timestamp.replace(year=_DUMMY_YEAR)
    return next(season for season, (start, end) in seasons_intervals
                if start <= timestamp <= end)