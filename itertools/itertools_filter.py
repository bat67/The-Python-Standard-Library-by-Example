#!/usr/bin/env python3
"""Using filter()
"""

#end_pymotw_header
from itertools import *


def check_item(x):
    print('Testing:', x)
    return x < 1


for i in filter(check_item, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)
