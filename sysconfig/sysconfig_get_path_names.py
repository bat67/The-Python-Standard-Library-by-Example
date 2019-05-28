#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""The names of the paths in a scheme.
"""

#end_pymotw_header
import sysconfig

for name in sysconfig.get_path_names():
    print(name)
