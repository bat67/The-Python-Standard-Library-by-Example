#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""


#end_pymotw_header
import tarfile

with tarfile.open('example.tar', 'r') as t:
    print(t.getnames())
