#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""


#end_pymotw_header
from http import cookies


c = cookies.SimpleCookie()
c['mycookie'] = 'cookie_value'
print(c)
