#!/usr/bin/env python3
# encoding: utf-8
#end_pymotw_header
import sys
import threading
import time

io_lock = threading.Lock()
blocker = threading.Lock()


def block(i):
    t = threading.current_thread()
    with io_lock:
        print('{} with ident {} going to sleep'.format(
            t.name, t.ident))
    if i:
        blocker.acquire()  # acquired but never released
        time.sleep(0.2)
    with io_lock:
        print(t.name, 'finishing')
    return


# Create and start several threads that "block"
threads = [
    threading.Thread(target=block, args=(i,))
    for i in range(3)
]
for t in threads:
    t.setDaemon(True)
    t.start()

# Map the threads from their identifier to the thread object
threads_by_ident = dict((t.ident, t) for t in threads)

# Show where each thread is "blocked"
time.sleep(0.01)
with io_lock:
    for ident, frame in sys._current_frames().items():
        t = threads_by_ident.get(ident)
        if not t:
            # Main thread
            continue
        print('{} stopped in {} at line {} of {}'.format(
            t.name, frame.f_code.co_name,
            frame.f_lineno, frame.f_code.co_filename))
