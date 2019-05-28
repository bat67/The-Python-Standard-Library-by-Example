#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import dis
import textwrap
import timeit


def add(words):
    result = ''
    for word in words:
        result = result + word
    return result


def add_inline(words):
    result = ''
    for word in words:
        result += word
    return result


def join(words):
    return ''.join(words)


if __name__ == '__main__':
    for fname in ['add', 'add_inline', 'join']:
        print('FUNCTION:', fname, '\n')
        f = globals()[fname]
        dis.dis(f)
        t = timeit.Timer(
            'd = {fname}(words)'.format(fname=fname),
            textwrap.dedent("""
            from dis_loops import {fname}
            words = [
                l.strip()
                for l in open('/usr/share/dict/words', 'rt')
            ]
            """).format(fname=fname),
        )
        iterations = 3
        print('TIME: {:0.4f}\n'.format(t.timeit(iterations)))
