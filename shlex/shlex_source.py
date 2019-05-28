#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
"""Including content from other files in the token stream.
"""

#end_pymotw_header
import shlex

text = "This text says to source quotes.txt before continuing."
print('ORIGINAL: {!r}'.format(text))
print()

lexer = shlex.shlex(text)
lexer.wordchars += '.'
lexer.source = 'source'

print('TOKENS:')
for token in lexer:
    print('{!r}'.format(token))
