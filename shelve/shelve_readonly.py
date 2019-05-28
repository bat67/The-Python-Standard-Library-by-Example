#!/usr/bin/env python3
"""Opening an existing shelf read-only.
"""

#end_pymotw_header
import dbm
import shelve

with shelve.open('test_shelf.db', flag='r') as s:
    print('Existing:', s['key1'])
    try:
        s['key1'] = 'new value'
    except dbm.error as err:
        print('ERROR: {}'.format(err))
