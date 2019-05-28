#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright 2007 Doug Hellmann.
#
"""Using sys.stderr for the prompt lets us redirect stdout.

"""

#end_pymotw_header
import getpass
import sys

p = getpass.getpass(stream=sys.stderr)
print('You entered:', p)
