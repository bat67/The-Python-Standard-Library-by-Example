#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#

import pdb


def f(n):
    for i in range(n):
        j = i * n
        print(i, j)
    return

if __name__ == '__main__':
    pdb.set_trace()
    f(5)
