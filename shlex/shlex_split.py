#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
"""Splitting strings with shlex.
"""

#end_pymotw_header
import shlex

text = """This text has "quoted parts" inside it."""
print('ORIGINAL: {!r}'.format(text))
print()

print('TOKENS:')
print(shlex.split(text))
