#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Random values from a range
"""

#end_pymotw_header
import random

for i in range(3):
    print(random.randrange(0, 101, 5), end=' ')
print()
