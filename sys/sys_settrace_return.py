#!/usr/bin/env python3
# encoding: utf-8

import sys


def trace_calls_and_returns(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from printing
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    if not filename.endswith('sys_settrace_return.py'):
        # Ignore calls not in this module
        return
    if event == 'call':
        print('* Call to {} on line {} of {}'.format(
            func_name, line_no, filename))
        return trace_calls_and_returns
    elif event == 'return':
        print('* {} => {}'.format(func_name, arg))
    return


def b():
    print('inside b()')
    return 'response_from_b '


def a():
    print('inside a()')
    val = b()
    return val * 2


sys.settrace(trace_calls_and_returns)
a()
