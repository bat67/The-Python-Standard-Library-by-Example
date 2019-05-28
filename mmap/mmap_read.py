#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Reading from a memory mapped file.
"""

#end_pymotw_header
import mmap

with open('lorem.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0,
                   access=mmap.ACCESS_READ) as m:
        print('First 10 bytes via read :', m.read(10))
        print('First 10 bytes via slice:', m[:10])
        print('2nd   10 bytes via read :', m.read(10))
