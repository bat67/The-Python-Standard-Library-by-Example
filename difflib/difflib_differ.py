#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Differ example
"""


#end_pymotw_header
import difflib
from difflib_data import *

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print('\n'.join(diff))
