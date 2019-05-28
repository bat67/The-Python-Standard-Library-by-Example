#!/usr/bin/env python3
"""atexit callbacks are not invoked if we bypass normal exit and
cleanup.

"""

# end_pymotw_header
import atexit
import os


def not_called():
    print('This should not be called')


print('Registering')
atexit.register(not_called)
print('Registered')

print('Exiting...')
os._exit(0)
