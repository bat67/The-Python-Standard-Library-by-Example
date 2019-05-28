#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Pretty print with pprint
"""

#end_pymotw_header
from pprint import pprint

from pprint_data import data

for width in [80, 5]:
    print('WIDTH =', width)
    pprint(data, width=width)
    print()
