#!/usr/bin/env python3
"""Simple example of using os.fork to create a new child process.
"""

#end_pymotw_header
import os

pid = os.fork()

if pid:
    print('Child process id:', pid)
else:
    print('I am the child')
