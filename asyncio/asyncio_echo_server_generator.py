#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""TCP echo server using asyncio with generator coroutines.
"""

#end_pymotw_header
import asyncio
import logging
import sys


@asyncio.coroutine
def echo(reader, writer):
    address = writer.get_extra_info('peername')
    log = logging.getLogger('echo_{}_{}'.format(*address))
    log.debug('connection accepted')
    while True:
        data = yield from reader.read(128)
        if data:
            log.debug('received {!r}'.format(data))
            writer.write(data)
            yield from writer.drain()
            log.debug('sent {!r}'.format(data))
        else:
            log.debug('closing')
            writer.close()
            return


logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)
log = logging.getLogger('main')

server_address = ('localhost', 10000)
event_loop = asyncio.get_event_loop()

# Create the server and let the loop finish the coroutine before
# starting the real event loop.
coroutine = asyncio.start_server(echo, *server_address,
                                 loop=event_loop)
server = event_loop.run_until_complete(coroutine)
log.debug('starting up on {} port {}'.format(*server_address))

# Enter the event loop permanently to handle all connections.
try:
    event_loop.run_forever()
finally:
    log.debug('closing server')
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    log.debug('closing event loop')
    event_loop.close()
