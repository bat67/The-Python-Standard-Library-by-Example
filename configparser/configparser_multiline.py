#!/usr/bin/env python3
#
# Copyright 2015 Doug Hellmann.
"""Example use of ConfigParser module.
"""

#end_pymotw_header
from configparser import ConfigParser
import os

filename = 'multiline.ini'
config = ConfigParser()
config.read([filename])

message = config['example']['message']

print(message)
