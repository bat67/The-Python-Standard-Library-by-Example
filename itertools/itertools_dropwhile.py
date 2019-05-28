#!/usr/bin/env python3
"""Using dropwhile()
"""

#end_pymotw_header
from itertools import *


def should_drop(x):
    print('Testing:', x)
    return x < 1


for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)
