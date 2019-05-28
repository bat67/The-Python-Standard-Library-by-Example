#!/usr/bin/env python3
"""Replacing os.system with subprocess.
"""

#end_pymotw_header
import subprocess

completed = subprocess.run(['ls', '-1'])
print('returncode:', completed.returncode)
