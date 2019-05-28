#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Generate random numbers
"""

#end_pymotw_header
import random

for i in range(5):
    print('%04.3f' % random.random(), end=' ')
print()
