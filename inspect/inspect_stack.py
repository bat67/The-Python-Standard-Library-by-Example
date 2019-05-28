#!/usr/bin/env python3
"""Inspecting the call stack.
"""

#end_pymotw_header
import inspect
import pprint


def show_stack():
    for level in inspect.stack():
        print('{}[{}]\n  -> {}'.format(
            level.frame.f_code.co_filename,
            level.lineno,
            level.code_context[level.index].strip(),
        ))
        pprint.pprint(level.frame.f_locals)
        print()


def recurse(limit):
    local_variable = '.' * limit
    if limit <= 0:
        show_stack()
        return
    recurse(limit - 1)
    return local_variable


if __name__ == '__main__':
    recurse(2)
