#!/usr/bin/env python3
# encoding: utf-8
#end_pymotw_header
import os
import sys

prefix = os.path.abspath(sys.prefix)

print('PATH:')
for name in sys.path:
    name = name.replace(prefix, '...')
    print(' ', name)

print()
print('IMPORTERS:')
for name, cache_value in sys.path_importer_cache.items():
    if '..' in name:
        name = os.path.abspath(name)
    name = name.replace(prefix, '...')
    print('  {}: {!r}'.format(name, cache_value))
