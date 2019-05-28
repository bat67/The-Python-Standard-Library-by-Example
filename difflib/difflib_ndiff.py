#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""ndiff example
"""

#end_pymotw_header
import difflib
from difflib_data import *

diff = difflib.ndiff(text1_lines, text2_lines)
print('\n'.join(diff))
