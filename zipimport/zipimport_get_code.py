#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Retrieving the code for a module within a zip archive.
"""

#end_pymotw_header
import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')
code = importer.get_code('zipimport_get_code')
print(code)
