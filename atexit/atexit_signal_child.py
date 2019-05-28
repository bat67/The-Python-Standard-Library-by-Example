#!/usr/bin/env python3
"""Child process in signal example.
"""

# end_pymotw_header
import atexit
import time
import sys


def not_called():
    print('CHILD: atexit handler should not have been called')


print('CHILD: Registering atexit handler')
sys.stdout.flush()
atexit.register(not_called)

print('CHILD: Pausing to wait for signal')
sys.stdout.flush()
time.sleep(5)
