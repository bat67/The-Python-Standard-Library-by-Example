#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Finding a module within a zip archive.
"""

#end_pymotw_header
import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')

for module_name in ['zipimport_find_module', 'not_there']:
    print(module_name, ':', importer.find_module(module_name))
