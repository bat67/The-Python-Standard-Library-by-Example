#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Stopping the event loop
"""

#end_pymotw_header
import asyncio
import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)
LOG = logging.getLogger('main')


async def stopper(loop):
    LOG.debug('stopper invoked')
    loop.stop()


event_loop = asyncio.get_event_loop()

event_loop.create_task(stopper(event_loop))

try:
    LOG.debug('entering event loop')
    event_loop.run_forever()
finally:
    LOG.debug('closing event loop')
    event_loop.close()
