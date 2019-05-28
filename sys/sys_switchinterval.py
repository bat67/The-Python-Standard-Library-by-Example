#!/usr/bin/env python3
# encoding: utf-8
#end_pymotw_header
import sys
import threading
from queue import Queue


def show_thread(q):
    for i in range(5):
        for j in range(1000000):
            pass
        q.put(threading.current_thread().name)
    return


def run_threads():
    interval = sys.getswitchinterval()
    print('interval = {:0.3f}'.format(interval))
    q = Queue()
    threads = [
        threading.Thread(target=show_thread,
                         name='T{}'.format(i),
                         args=(q,))
        for i in range(3)
    ]
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    while not q.empty():
        print(q.get(), end=' ')
    print()
    return


for interval in [0.001, 0.1]:
    sys.setswitchinterval(interval)
    run_threads()
    print()
