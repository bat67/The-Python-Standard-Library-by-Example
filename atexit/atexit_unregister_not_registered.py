#!/usr/bin/env python3
"""Cancel registered callback
"""
# end_pymotw_header
import atexit


def my_cleanup(name):
    print('my_cleanup({})'.format(name))


if False:
    atexit.register(my_cleanup, 'never registered')

atexit.unregister(my_cleanup)
