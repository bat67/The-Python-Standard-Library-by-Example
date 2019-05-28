#!/usr/bin/env python3
#
# Copyright 2010 Doug Hellmann.
#
"""Checking exit codes from external processes
"""

#end_pymotw_header
import subprocess

try:
    subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
