#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Pretty print with pprint
"""

#end_pymotw_header
from pprint import pprint

from pprint_data import data

print('PRINT:')
print(data)
print()
print('PPRINT:')
pprint(data)
