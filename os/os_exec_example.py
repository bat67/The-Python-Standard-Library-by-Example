#!/usr/bin/env python3
"""Using os.exec*().
"""

#end_pymotw_header
import os

child_pid = os.fork()
if child_pid:
    os.waitpid(child_pid, 0)
else:
    os.execlp('pwd', 'pwd', '-P')
