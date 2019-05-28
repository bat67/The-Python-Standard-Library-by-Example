#!/usr/bin/env python3
"""Running a command in the background
"""

#end_pymotw_header
import os
import time

print('Calling...')
os.system('date; (sleep 3; date) &')

print('Sleeping...')
time.sleep(5)
