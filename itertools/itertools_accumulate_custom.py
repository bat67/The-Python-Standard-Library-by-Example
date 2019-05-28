#!/usr/bin/env python3
# encoding: utf-8
"""combine values
"""

#end_pymotw_header
from itertools import *


def f(a, b):
    print(a, b)
    return b + a + b


print(list(accumulate('abcde', f)))
