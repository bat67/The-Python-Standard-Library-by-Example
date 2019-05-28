#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright 2007 Doug Hellmann.
#
"""Passing a prompt to getpass.

"""

#end_pymotw_header
import getpass

p = getpass.getpass(prompt='What is your favorite color? ')
if p.lower() == 'blue':
    print('Right.  Off you go.')
else:
    print('Auuuuugh!')
