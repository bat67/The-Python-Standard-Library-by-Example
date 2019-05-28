#!/usr/bin/env python3
"""Print entire year calendar.
"""
#end_pymotw_header
import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatyear(2017, 2, 1, 1, 3))
