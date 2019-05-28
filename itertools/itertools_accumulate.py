#!/usr/bin/env python3
# encoding: utf-8
"""combine values
"""

#end_pymotw_header
from itertools import *

print(list(accumulate(range(5))))
print(list(accumulate('abcde')))
