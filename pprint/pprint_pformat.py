#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Formatting with pformat
"""

#end_pymotw_header
import logging
from pprint import pformat
from pprint_data import data

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s %(message)s',
)

logging.debug('Logging pformatted data')
formatted = pformat(data)
for line in formatted.splitlines():
    logging.debug(line.rstrip())
