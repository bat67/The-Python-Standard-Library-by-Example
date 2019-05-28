#!/usr/bin/env python3
# encoding: utf-8
#
# Turn off flake8 tests for this file because it is apparently not
# possible to skip only the one for long lines:
# flake8: noqa
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Telling doctest to ignore extra whitespace in test data.
"""
#end_pymotw_header
def my_function(a, b):
    """Returns a * b.

    >>> my_function(['A', 'B'], 3) #doctest: +NORMALIZE_WHITESPACE
    ['A', 'B',
     'A', 'B',
     'A', 'B']

    This does not match because of the extra space after the [ in
    the list.

    >>> my_function(['A', 'B'], 2) #doctest: +NORMALIZE_WHITESPACE
    [ 'A', 'B',
      'A', 'B', ]
    """
    return a * b
