#!/usr/bin/env python3
"""Show the comment before a method.
"""

#end_pymotw_header
import inspect
import example

print(inspect.getcomments(example))
