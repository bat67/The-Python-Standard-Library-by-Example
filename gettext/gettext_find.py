#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import gettext

catalogs = gettext.find('example', 'locale', all=True)
print('Catalogs:', catalogs)
