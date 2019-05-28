#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Show the user base directory.
"""

#end_pymotw_header
import site

print('Base:', site.USER_BASE)
print('Site:', site.USER_SITE)
