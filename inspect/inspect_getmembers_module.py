#!/usr/bin/env python3
"""Using getmembers()
"""

#end_pymotw_header
import inspect

import example

for name, data in inspect.getmembers(example):
    if name.startswith('__'):
        continue
    print('{} : {!r}'.format(name, data))
