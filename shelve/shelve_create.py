#!/usr/bin/env python3
"""Creating a new shelf.
"""

#end_pymotw_header
import shelve

with shelve.open('test_shelf.db') as s:
    s['key1'] = {
        'int': 10,
        'float': 9.5,
        'string': 'Sample data',
    }
