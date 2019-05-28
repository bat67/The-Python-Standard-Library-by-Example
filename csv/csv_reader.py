#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Example of reading a comma separated value file.
"""
#end_pymotw_header
import csv
import sys

with open(sys.argv[1], 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
