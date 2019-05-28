#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright 2009 Doug Hellmann.
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
import grp
import textwrap

# Load all of the user data, sorted by username
all_groups = grp.getgrall()
interesting_groups = {
    g.gr_name: g
    for g in all_groups
    if not g.gr_name.startswith('_')
}
print(len(interesting_groups.keys()))

# Find the longest length for a few fields
name_length = max(len(k) for k in interesting_groups) + 1
gid_length = max(len(str(u.gr_gid))
                 for u in interesting_groups.values()) + 1

# Set the members field width to avoid table columns
# wrapping
members_width = 19

# Print report headers
fmt = ' '.join(['{:<{name_length}}',
                '{:{gid_length}}',
                '{:<{members_width}}',
                ])
print(fmt.format('Name',
                 'GID',
                 'Members',
                 name_length=name_length,
                 gid_length=gid_length,
                 members_width=members_width))
print('-' * name_length,
      '-' * gid_length,
      '-' * members_width)

# Print the data
prefix = ' ' * (name_length + gid_length + 2)
for name, g in sorted(interesting_groups.items()):
    # Format members to start in the column on the same line but
    # wrap as needed with an indent sufficient to put the
    # subsequent lines in the members column. The two indent
    # prefixes need to be the same to compute the wrap properly,
    # but the first should not be printed so strip it.
    members = textwrap.fill(
        ', '.join(g.gr_mem),
        initial_indent=prefix,
        subsequent_indent=prefix,
        width=members_width + len(prefix),
    ).strip()
    print(fmt.format(g.gr_name,
                     g.gr_gid,
                     members,
                     name_length=name_length,
                     gid_length=gid_length,
                     members_width=members_width))
