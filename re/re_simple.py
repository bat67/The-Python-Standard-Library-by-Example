#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Simple pattern examples.
"""

#end_pymotw_header
import re

patterns = ['this', 'that']
text = 'Does this text match the pattern?'

print('Text: {!r}\n'.format(text))

for pattern in patterns:
    print('Seeking "{}" ->'.format(pattern), end=' ')

    if re.search(pattern, text) is None:
        print('no match')
    else:
        print('match!')
