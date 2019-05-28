#!/usr/bin/env python3
"""Using chain()
"""

#end_pymotw_header
from itertools import *

for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print(i, end=' ')
print()
