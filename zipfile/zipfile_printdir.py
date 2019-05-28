#!/usr/bin/env python3
"""Print the table of contents of a ZIP archive
"""

#end_pymotw_header
import zipfile

with zipfile.ZipFile('example.zip', 'r') as zf:
    print(zf.printdir())
