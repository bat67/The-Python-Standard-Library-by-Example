#!/usr/bin/env python3
# encoding: utf-8
#end_pymotw_header
import sys
import textwrap

names = sorted(sys.modules.keys())
name_text = ', '.join(names)

print(textwrap.fill(name_text, width=64))
