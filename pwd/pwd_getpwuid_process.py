#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import pwd
import os

uid = os.getuid()
user_info = pwd.getpwuid(uid)
print('Currently running with UID={} username={}'.format(
    uid, user_info.pw_name))
