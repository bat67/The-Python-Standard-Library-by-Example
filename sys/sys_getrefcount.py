#!/usr/bin/env python3
# encoding: utf-8
#end_pymotw_header
import sys

one = []
print('At start         :', sys.getrefcount(one))

two = one

print('Second reference :', sys.getrefcount(one))

del two

print('After del        :', sys.getrefcount(one))
