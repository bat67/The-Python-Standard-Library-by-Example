#!/usr/bin/env python3
"""Using repeat() and map()
"""

#end_pymotw_header
from itertools import *

for i in map(lambda x, y: (x, y, x * y), repeat(2), range(5)):
    print('{:d} * {:d} = {:d}'.format(*i))
