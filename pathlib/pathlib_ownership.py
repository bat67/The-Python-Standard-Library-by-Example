#!/usr/bin/env python3
"""Show stat info for a file.
"""

#end_pymotw_header
import pathlib

p = pathlib.Path(__file__)

print('{} is owned by {}/{}'.format(p, p.owner(), p.group()))
