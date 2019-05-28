#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Retrieving the code for a module within a zip archive.
"""

#end_pymotw_header
import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')
module = importer.load_module('zipimport_get_code')
print('Name   :', module.__name__)
print('Loader :', module.__loader__)
print('Code   :', module.code)
