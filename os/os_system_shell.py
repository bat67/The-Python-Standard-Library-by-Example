#!/usr/bin/env python3
"""Using os.system() to run external commands.
"""

#end_pymotw_header
import os

# Command with shell expansion
os.system('echo $TMPDIR')
