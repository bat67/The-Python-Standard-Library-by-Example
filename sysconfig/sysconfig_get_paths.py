#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""The paths for a scheme.
"""

#end_pymotw_header
import sysconfig
import pprint
import os

for scheme in ['posix_prefix', 'posix_user']:
    print(scheme)
    print('=' * len(scheme))
    paths = sysconfig.get_paths(scheme=scheme)
    prefix = os.path.commonprefix(list(paths.values()))
    print('prefix = {}\n'.format(prefix))
    for name, path in sorted(paths.items()):
        print('{}\n  .{}'.format(name, path[len(prefix):]))
    print()
