#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Which archive formats are supported?
"""

#end_pymotw_header
import shutil

for format, description in shutil.get_archive_formats():
    print('{:<5}: {}'.format(format, description))
