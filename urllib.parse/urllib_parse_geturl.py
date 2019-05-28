#!/usr/bin/env python3
"""Parsing URLs
"""

#end_pymotw_header
from urllib.parse import urlparse

original = 'http://netloc/path;param?query=arg#frag'
print('ORIG  :', original)
parsed = urlparse(original)
print('PARSED:', parsed.geturl())
