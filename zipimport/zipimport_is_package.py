#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Determine whether the type of a module within a ZIP archive
"""

#end_pymotw_header
import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')
for name in ['zipimport_is_package', 'example_package']:
    print(name, importer.is_package(name))
