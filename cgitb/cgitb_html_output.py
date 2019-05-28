#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""Generate a traceback with more details.
"""

#end_pymotw_header
import cgitb
cgitb.enable()


def func1(arg1):
    local_var = arg1 * 2
    return func2(local_var)


def func2(arg2):
    local_var = arg2 + 2
    return func3(local_var)


def func3(arg3):
    local_var = arg2 / 2  # noqa
    return local_var

func1(1)
