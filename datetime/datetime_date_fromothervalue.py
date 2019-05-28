#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Creating datetime.date() instances from other types of values.
"""

#end_pymotw_header
import datetime
import time

o = 733114
print('o:', o)
print('fromordinal(o):', datetime.date.fromordinal(o))
t = time.time()
print('t:', t)
print('fromtimestamp(t):', datetime.date.fromtimestamp(t))
