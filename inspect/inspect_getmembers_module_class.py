#!/usr/bin/env python3
"""Using getmembers()
"""

#end_pymotw_header
import inspect

import example

for name, data in inspect.getmembers(example, inspect.isclass):
    print('{} : {!r}'.format(name, data))
