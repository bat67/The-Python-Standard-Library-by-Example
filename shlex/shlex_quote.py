#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
"""Differences between POSIX and non-POSIX parsing.
"""

#end_pymotw_header
import shlex

examples = [
    "Embedded'SingleQuote",
    'Embedded"DoubleQuote',
    'Embedded Space',
    '~SpecialCharacter',
    r'Back\slash',
]

for s in examples:
    print('ORIGINAL : {}'.format(s))
    print('QUOTED   : {}'.format(shlex.quote(s)))
    print()
