#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
"""Example use of ConfigParser module.
"""

#end_pymotw_header
from configparser import ConfigParser
import os

filename = 'approach.ini'
config = ConfigParser()
config.read([filename])

url = config.get('portal', 'url')

print(url)
