#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Tuning the garbage collector threshold.
"""

#end_pymotw_header
import gc

gc.set_debug(gc.DEBUG_STATS)

gc.collect()
print('Exiting')
