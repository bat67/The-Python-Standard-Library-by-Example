#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Pretty print with pprint
"""

#end_pymotw_header
from pprint import pprint

from pprint_data import data

print('DEFAULT:')
pprint(data, compact=False)
print('\nCOMPACT:')
pprint(data, compact=True)
