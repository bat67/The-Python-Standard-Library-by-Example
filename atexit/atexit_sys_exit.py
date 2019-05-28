#!/usr/bin/env python3
"""
"""

# end_pymotw_header
import atexit
import sys


def all_done():
    print('all_done()')


print('Registering')
atexit.register(all_done)
print('Registered')

print('Exiting...')
sys.exit()
