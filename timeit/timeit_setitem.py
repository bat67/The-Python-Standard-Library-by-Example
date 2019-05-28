#!/usr/bin/env python3
"""
"""

#end_pymotw_header

def test_setitem(range_size=1000):
    l = [(str(x), x) for x in range(range_size)]
    d = {}
    for s, i in l:
        d[s] = i
