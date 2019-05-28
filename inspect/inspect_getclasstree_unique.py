#!/usr/bin/env python3
"""
"""

#end_pymotw_header
import inspect
import example
from inspect_getclasstree import *

print_class_tree(inspect.getclasstree(
    [example.A, example.B, C, D],
    unique=True,
))
