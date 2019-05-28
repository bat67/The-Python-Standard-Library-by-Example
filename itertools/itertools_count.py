#!/usr/bin/env python3
"""Using count()
"""

#end_pymotw_header
from itertools import *

for i in zip(count(1), ['a', 'b', 'c']):
    print(i)
