#!/usr/bin/env python3
"""Docstrings
"""

#end_pymotw_header
import inspect
import example

print('B.__doc__:')
print(example.B.__doc__)
print()
print('getdoc(B):')
print(inspect.getdoc(example.B))
