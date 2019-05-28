#!/usr/bin/env python3
"""Writing data to a new archive.
"""

#end_pymotw_header
from zipfile_infolist import print_info
import zipfile

print('creating archive')
with zipfile.ZipFile('write.zip', mode='w') as zf:
    print('adding README.txt')
    zf.write('README.txt')

print()
print_info('write.zip')
