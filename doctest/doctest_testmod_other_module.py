#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Run tests for another module we import.
"""

#end_pymotw_header
import doctest_simple

if __name__ == '__main__':
    import doctest
    doctest.testmod(doctest_simple)
