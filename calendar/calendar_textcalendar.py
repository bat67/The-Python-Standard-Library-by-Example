#!/usr/bin/env python3
"""Sample of TextCalendar output.
"""
#end_pymotw_header
import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2017, 7)
