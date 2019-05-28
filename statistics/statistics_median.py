#!/usr/bin/env python3
# encoding: utf-8
#
"""
"""

#end_pymotw_header
from statistics import *

data = [1, 2, 2, 5, 10, 12]

print('median     : {:0.2f}'.format(median(data)))
print('low        : {:0.2f}'.format(median_low(data)))
print('high       : {:0.2f}'.format(median_high(data)))
