#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Split fractional from whole number part.
"""

#end_pymotw_header
import math

for i in range(6):
    print('{}/2 = {}'.format(i, math.modf(i / 2.0)))
