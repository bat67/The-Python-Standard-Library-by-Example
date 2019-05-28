#!/usr/bin/env python3
"""Handling parse errors.
"""

#end_pymotw_header
import shlex

text = """This line is ok.
This line has an "unfinished quote.
This line is ok, too.
"""

print('ORIGINAL: {!r}'.format(text))
print()

lexer = shlex.shlex(text)

print('TOKENS:')
try:
    for token in lexer:
        print('{!r}'.format(token))
except ValueError as err:
    first_line_of_error = lexer.token.splitlines()[0]
    print('ERROR: {} {}'.format(lexer.error_leader(), err))
    print('following {!r}'.format(first_line_of_error))
