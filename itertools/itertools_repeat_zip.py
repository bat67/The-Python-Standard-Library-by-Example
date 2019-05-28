#!/usr/bin/env python3
"""Using repeat() with zip().
"""

#end_pymotw_header
from itertools import *

for i, s in zip(count(), repeat('over-and-over', 5)):
    print(i, s)
