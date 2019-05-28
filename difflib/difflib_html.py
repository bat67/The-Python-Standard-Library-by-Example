#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""HtmlDiff example
"""


#end_pymotw_header
import difflib
from difflib_data import *

d = difflib.HtmlDiff()
print(d.make_table(text1_lines, text2_lines))
