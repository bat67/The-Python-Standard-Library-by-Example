#!/usr/bin/env python3
# encoding: utf-8
#end_pymotw_header
import sys


class LineCounter:

    def __init__(self):
        self.count = 0

    def __str__(self):
        self.count += 1
        return '({:3d})> '.format(self.count)
