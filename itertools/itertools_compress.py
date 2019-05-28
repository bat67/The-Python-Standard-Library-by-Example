#!/usr/bin/env python3
"""Using filter()
"""

#end_pymotw_header
from itertools import *

every_third = cycle([False, False, True])
data = range(1, 10)

for i in compress(data, every_third):
    print(i, end=' ')
print()
