#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Handling recursive data structures.
"""

#end_pymotw_header
from pprint import pprint

local_data = ['a', 'b', 1, 2]
local_data.append(local_data)

print('id(local_data) =>', id(local_data))
pprint(local_data)
