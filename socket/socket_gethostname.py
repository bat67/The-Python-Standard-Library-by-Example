#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Look up the name of the current host
"""

#end_pymotw_header
import socket

print(socket.gethostname())
