#!/usr/bin/env python3
"""A simple recursive directory listing.
"""

#end_pymotw_header
import os
import sys

# If we are not given a path to list, use /tmp
if len(sys.argv) == 1:
    root = '/tmp'
else:
    root = sys.argv[1]

for dir_name, sub_dirs, files in os.walk(root):
    print(dir_name)
    # Make the subdirectory names stand out with /
    sub_dirs = [n + '/' for n in sub_dirs]
    # Mix the directory contents together
    contents = sub_dirs + files
    contents.sort()
    # Show the contents
    for c in contents:
        print('  {}'.format(c))
    print()
