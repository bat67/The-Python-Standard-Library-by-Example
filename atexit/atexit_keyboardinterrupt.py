#!/usr/bin/env python3
"""atexit functions are still called when a KeyboardInterrupt is
received.

"""
# end_pymotw_header
import atexit
import sys


def is_called():
    print('The atexit handlers are still called')


atexit.register(is_called)

sys.stdout.write('Press Ctrl-C now')
sys.stdout.flush()

ignored = sys.stdin.readline()
