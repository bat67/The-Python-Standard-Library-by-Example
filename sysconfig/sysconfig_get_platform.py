#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Platform specifier for binary modules
"""

#end_pymotw_header
import sysconfig

print(sysconfig.get_platform())
