#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Retrieving data when there is no ZIP archive involved.
"""

#end_pymotw_header
import os
import example_package

# Find the directory containing the imported
# package and build the data filename from it.
pkg_dir = os.path.dirname(example_package.__file__)
data_filename = os.path.join(pkg_dir, 'README.txt')

# Read the file and show its contents.
print(data_filename, ':')
print(open(data_filename, 'r').read())
