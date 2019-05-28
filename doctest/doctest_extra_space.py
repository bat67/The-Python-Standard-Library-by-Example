#!/usr/bin/env python3
# encoding: utf-8
#
# Turn off flake8 tests for this file because it is apparently not
# possible to skip only the one for trailing whitespace:
# flake8: noqa
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Whitespace at the end of a line can cause a mis-match.
"""
#end_pymotw_header
def my_function(a, b):
    """
    >>> my_function(2, 3)
    6 
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b
