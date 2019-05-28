#!/usr/bin/env python3
# encoding: utf-8
#end_pymotw_header
import sys


def my_excepthook(type, value, traceback):
    print('Unhandled error:', type, value)


sys.excepthook = my_excepthook

print('Before exception')

raise RuntimeError('This is the error message')

print('After exception')
