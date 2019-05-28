#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Importing a module from a package
"""

#end_pymotw_header
import importlib


try:
    importlib.import_module('example.nosuchmodule')
except ImportError as err:
    print('Error:', err)
