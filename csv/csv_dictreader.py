#!/usr/bin/env python3

"""Dictionary reader.
"""
#end_pymotw_header
import csv
import sys

with open(sys.argv[1], 'rt') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
