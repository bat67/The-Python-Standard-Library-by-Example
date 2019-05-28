#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Installation schemes.
"""

#end_pymotw_header
import sysconfig

for name in sysconfig.get_scheme_names():
    print(name)
