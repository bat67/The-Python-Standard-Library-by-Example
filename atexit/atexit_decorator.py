#!/usr/bin/env python3
"""Using atexit.register as a decorator.
"""
# end_pymotw_header
import atexit


@atexit.register
def all_done():
    print('all_done()')


print('starting main program')
