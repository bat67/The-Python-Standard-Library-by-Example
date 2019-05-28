#!/usr/bin/env python3
"""A simple directory listing.
"""

#end_pymotw_header
import os
import sys

print(sorted(os.listdir(sys.argv[1])))
