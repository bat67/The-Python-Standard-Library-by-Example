#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Retrieving the data for a module within a zip archive.
"""

#end_pymotw_header
import sys
sys.path.insert(0, 'zipimport_example.zip')

import os
import example_package
print(example_package.__file__)
data_filename = os.path.join(
    os.path.dirname(example_package.__file__),
    'README.txt',
)
print(data_filename, ':')
print(open(data_filename, 'rt').read())
