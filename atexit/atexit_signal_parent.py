#!/usr/bin/env python3
"""Send a signal to a child process, killing it, to illustrate
that the atexit handlers are not called.

"""

# end_pymotw_header
import os
import signal
import subprocess
import time

proc = subprocess.Popen('./atexit_signal_child.py')
print('PARENT: Pausing before sending signal...')
time.sleep(1)
print('PARENT: Signaling child')
os.kill(proc.pid, signal.SIGTERM)
