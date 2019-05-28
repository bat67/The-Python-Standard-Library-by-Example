#!/usr/bin/env python3
"""If an exception is raised in an atexit callback, it is
printed to the console.

"""
# end_pymotw_header
import atexit


def exit_with_exception(message):
    raise RuntimeError(message)


atexit.register(exit_with_exception, 'Registered first')
atexit.register(exit_with_exception, 'Registered second')
