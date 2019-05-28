#!/usr/bin/env python3
"""Opening an existing shelf.
"""

#end_pymotw_header
import shelve

with shelve.open('test_shelf.db') as s:
    existing = s['key1']

print(existing)
