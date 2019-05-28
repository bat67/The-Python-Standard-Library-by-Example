#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#


def f(n):
    if n < 0:
        raise ValueError('Invalid n: {}'.format(n))
    result = []
    j = 0
    for i in range(n):
        j = i * n + j
        j += n
        result.append(j)
    return result


if __name__ == '__main__':
    try:
        print(f(5))
    finally:
        print('Always printed')

    try:
        print(f(-5))
    except:
        print('There was an error')
    else:
        print('There was no error')

    print('Last statement')
