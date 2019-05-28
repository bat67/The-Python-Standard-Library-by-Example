#!/usr/bin/env python3
"""Sample of TextCalendar output.
"""
#end_pymotw_header
import calendar

c = calendar.LocaleTextCalendar(locale='en_US')
c.prmonth(2017, 7)

print()

c = calendar.LocaleTextCalendar(locale='fr_FR')
c.prmonth(2017, 7)
