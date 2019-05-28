#!/usr/bin/env python3
"""Joining relative fragments into absolute URLs
"""

#end_pymotw_header
from urllib.parse import urljoin

print(urljoin('http://www.example.com/path/file.html',
              'anotherfile.html'))
print(urljoin('http://www.example.com/path/file.html',
              '../anotherfile.html'))
