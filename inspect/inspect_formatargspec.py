#!/usr/bin/env python3
"""Print information about the arguments to a method.
"""


#end_pymotw_header
import inspect
import example

spec = inspect.getargspec(example.module_level_function)
print(spec)
print(inspect.formatargspec(spec))
