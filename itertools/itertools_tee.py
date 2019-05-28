#!/usr/bin/env python3
"""Using tee()
"""

#end_pymotw_header
from itertools import *

r = islice(count(), 5)
i1, i2 = tee(r)

print('i1:', list(i1))
print('i2:', list(i2))
