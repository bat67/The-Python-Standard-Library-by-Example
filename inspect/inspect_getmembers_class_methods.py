#!/usr/bin/env python3
"""Using getmembers()
"""

#end_pymotw_header
import inspect
from pprint import pprint

import example

pprint(inspect.getmembers(example.A, inspect.isfunction))
