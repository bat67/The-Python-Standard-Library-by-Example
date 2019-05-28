#!/usr/bin/env python3
"""Simple logging to stderr using different levels.
"""

#end_pymotw_header
import logging
import warnings

logging.basicConfig(
    level=logging.INFO,
)

warnings.warn('This warning is not sent to the logs')

logging.captureWarnings(True)

warnings.warn('This warning is sent to the logs')
