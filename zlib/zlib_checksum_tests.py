#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import textwrap
import timeit

iterations = 1000


def show_results(title, result, iterations):
    "Report microseconds per pass and per item."
    per_pass = 1000000 * (result / iterations)
    print('{}:  {:0.2f} usec/pass'.format(title, per_pass))


adler32 = timeit.Timer(
    stmt="zlib.adler32(data)",
    setup=textwrap.dedent("""\
    import zlib
    data=open('lorem.txt','r').read() * 10
    """),
)
show_results('Adler32, separate',
             adler32.timeit(iterations), iterations)

adler32_running = timeit.Timer(
    stmt="cksum = zlib.adler32(data, cksum)",
    setup=textwrap.dedent("""\
    import zlib
    data=open('lorem.txt','r').read() * 10
    cksum = zlib.adler32(data)
    """),
)
show_results('Adler32, running',
             adler32_running.timeit(iterations), iterations)

crc32 = timeit.Timer(
    stmt="zlib.crc32(data)",
    setup=textwrap.dedent("""\
    import zlib
    data=open('lorem.txt','r').read() * 10
    """),
)
show_results('CRC-32, separate',
             crc32.timeit(iterations), iterations)

crc32_running = timeit.Timer(
    stmt="cksum = zlib.crc32(data, cksum)",
    setup=textwrap.dedent("""\
    import zlib
    data=open('lorem.txt','r').read() * 10
    cksum = zlib.crc32(data)
    """),
)
show_results('CRC-32, running',
             crc32_running.timeit(iterations), iterations)
