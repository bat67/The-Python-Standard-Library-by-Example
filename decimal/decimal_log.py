#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import decimal

d = decimal.Decimal(100)
print('d     :', d)
print('log10 :', d.log10())
print('ln    :', d.ln())
