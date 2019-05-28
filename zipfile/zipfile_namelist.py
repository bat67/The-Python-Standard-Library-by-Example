#!/usr/bin/env python3
"""Reading the names out of a ZIP archive.
"""

#end_pymotw_header
import zipfile

with zipfile.ZipFile('example.zip', 'r') as zf:
    print(zf.namelist())
