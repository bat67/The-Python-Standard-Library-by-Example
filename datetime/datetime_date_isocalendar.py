#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Demonstrate the ISO calendar features of date().
"""

#end_pymotw_header
import datetime
import locale

day_names = [
    locale.nl_langinfo(x)
    for x in (locale.DAY_1, locale.DAY_2, locale.DAY_3,
              locale.DAY_4, locale.DAY_5, locale.DAY_6,
              locale.DAY_7, locale.DAY_1)
]

print('US days :', day_names[:-1])
print('ISO days:', day_names[1:])

d = datetime.date(2007, 12, 30)
for i in range(7):
    delta = datetime.timedelta(days=i)
    date = d + delta
    print()
    print(day_names[date.weekday()], date)
    print('  ISO Weekday:', day_names[date.isoweekday()])
    print('  ISO Calendar:', date.isocalendar())
