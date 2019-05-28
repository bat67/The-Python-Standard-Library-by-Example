#!/usr/bin/env python3
# encoding: utf-8
#end_pymotw_header
import sys

print('Initial limit:', sys.getrecursionlimit())

sys.setrecursionlimit(10)

print('Modified limit:', sys.getrecursionlimit())


def generate_recursion_error(i):
    print('generate_recursion_error({})'.format(i))
    generate_recursion_error(i + 1)


try:
    generate_recursion_error(1)
except RuntimeError as err:
    print('Caught exception:', err)
