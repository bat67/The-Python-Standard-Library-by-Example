#!/usr/bin/env python3
"""Example of using timeit programatically.

Time various ways to populate and check a dictionary
using a long list of strings and integers.
"""

#end_pymotw_header
import timeit

# using setitem
t = timeit.Timer("print('main statement')", "print('setup')")

print('TIMEIT:')
print(t.timeit(2))

print('REPEAT:')
print(t.repeat(3, 2))
