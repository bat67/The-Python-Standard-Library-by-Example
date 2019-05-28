#!/usr/bin/env python3
"""Using spawn*() instead of fork() and exec*().
"""

#end_pymotw_header
import os

os.spawnlp(os.P_WAIT, 'pwd', 'pwd', '-P')
