#!/usr/bin/env python3
"""Using filterfalse()
"""

#end_pymotw_header
from itertools import *


def check_item(x):
    print('Testing:', x)
    return x < 1


for i in filterfalse(check_item, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)
