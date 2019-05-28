#!/usr/bin/env python3
"""Modifying an existing shelf opened with write-back enabled.
"""

#end_pymotw_header
import shelve

with shelve.open('test_shelf.db') as s:
    print(s['key1'])
    s['key1']['new_value'] = 'this was not here before'

with shelve.open('test_shelf.db', writeback=True) as s:
    print(s['key1'])
