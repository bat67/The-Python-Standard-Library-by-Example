#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""pathlib glob
"""

#end_pymotw_header
import pathlib

p = pathlib.Path('..')

for f in p.glob('*.rst'):
    print(f)
