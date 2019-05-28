#!/usr/bin/env python3
"""Sample of TextCalendar output.
"""
#end_pymotw_header
import calendar

c = calendar.HTMLCalendar(calendar.SUNDAY)
print(c.formatmonth(2017, 7))
