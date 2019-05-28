#!/usr/bin/env python3
"""Generate a base64 encoded HMAC signature.
"""

#end_pymotw_header
import base64
import hmac
import hashlib

with open('lorem.txt', 'rb') as f:
    body = f.read()

hash = hmac.new(
    b'secret-shared-key-goes-here',
    body,
    hashlib.sha1,
)

digest = hash.digest()
print(base64.encodebytes(digest))
