#!/usr/bin/env python3
"""Find information about the current process.
"""

#end_pymotw_header
import os

print('This process id:', os.getpid())
print('Parent process :', os.getppid())
print('Process group  :', os.getpgid(os.getpid()))
print('Parent group   :', os.getpgid(os.getppid()))
print('Session id     :', os.getsid(0))
