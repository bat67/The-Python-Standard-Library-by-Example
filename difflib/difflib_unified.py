#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Unified diff example
"""


#end_pymotw_header
import difflib
from difflib_data import *

diff = difflib.unified_diff(
    text1_lines,
    text2_lines,
    lineterm='',
)
print('\n'.join(diff))
