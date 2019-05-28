#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Context diff example
"""

#end_pymotw_header
import difflib
from difflib_data import *

diff = difflib.context_diff(
    text1_lines,
    text2_lines,
    lineterm='',
)
print('\n'.join(diff))
