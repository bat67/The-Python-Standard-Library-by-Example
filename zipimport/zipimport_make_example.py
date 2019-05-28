#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Create a sample zipfile with modules that can be imported.
"""

#end_pymotw_header
import sys
import zipfile

if __name__ == '__main__':
    zf = zipfile.PyZipFile('zipimport_example.zip', mode='w')
    try:
        zf.writepy('.')
        zf.write('zipimport_get_source.py')
        zf.write('example_package/README.txt')
    finally:
        zf.close()
    for name in zf.namelist():
        print(name)
