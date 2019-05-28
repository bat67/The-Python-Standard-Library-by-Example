#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright 2013 Doug Hellmann.
#
#
#                         All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software
# and its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of
# Doug Hellmann not be used in advertising or publicity
# pertaining to distribution of the software without specific,
# written prior permission.
#
# DOUG HELLMANN DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
# SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS, IN NO EVENT SHALL DOUG HELLMANN BE LIABLE FOR ANY
# SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION,
# ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF
# THIS SOFTWARE.
#
"""
"""


#end_pymotw_header
import pwd
import operator

# Load all of the user data, sorted by username
all_user_data = pwd.getpwall()
interesting_users = sorted(
    (u for u in all_user_data
     if not u.pw_name.startswith('_')),
    key=operator.attrgetter('pw_name')
)

# Find the longest lengths for a few fields
username_length = max(len(u.pw_name)
                      for u in interesting_users) + 1
home_length = max(len(u.pw_dir)
                  for u in interesting_users) + 1
uid_length = max(len(str(u.pw_uid))
                 for u in interesting_users) + 1

# Print report headers
fmt = ' '.join(['{:<{username_length}}',
                '{:>{uid_length}}',
                '{:<{home_length}}',
                '{}'])
print(fmt.format('User',
                 'UID',
                 'Home Dir',
                 'Description',
                 username_length=username_length,
                 uid_length=uid_length,
                 home_length=home_length))
print('-' * username_length,
      '-' * uid_length,
      '-' * home_length,
      '-' * 20)

# Print the data
for u in interesting_users:
    print(fmt.format(u.pw_name,
                     u.pw_uid,
                     u.pw_dir,
                     u.pw_gecos,
                     username_length=username_length,
                     uid_length=uid_length,
                     home_length=home_length))
