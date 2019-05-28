#!/usr/bin/env python3
"""Using getmembers()
"""

#end_pymotw_header
import inspect
from pprint import pprint

import example

a = example.A(name='inspect_getmembers')
pprint(inspect.getmembers(a, inspect.ismethod))
