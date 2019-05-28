#!/usr/bin/env python3
"""Using the os module to read and write environment variables.
"""

#end_pymotw_header
import os

print('Starting:', os.getcwd())

print('Moving up one:', os.pardir)
os.chdir(os.pardir)

print('After move:', os.getcwd())
