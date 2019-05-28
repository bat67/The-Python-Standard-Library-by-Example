#!/usr/bin/env python3
"""
"""

#end_pymotw_header
import inspect
import pprint
import example

pprint.pprint(inspect.getsourcelines(example.A.get_name))
