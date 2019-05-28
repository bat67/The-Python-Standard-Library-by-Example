#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
"""Other uses for the parser.
"""

#end_pymotw_header
import shlex

text = """|Col 1||Col 2||Col 3|"""
print('ORIGINAL: {!r}'.format(text))
print()

lexer = shlex.shlex(text)
lexer.quotes = '|'

print('TOKENS:')
for token in lexer:
    print('{!r}'.format(token))
