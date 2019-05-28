#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""


#end_pymotw_header
import platform

print('interpreter:', platform.architecture())
print('/bin/ls    :', platform.architecture('/bin/ls'))
