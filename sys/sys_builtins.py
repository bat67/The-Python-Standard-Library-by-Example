#!/usr/bin/env python3
# encoding: utf-8
#end_pymotw_header
import sys
import textwrap

name_text = ', '.join(sorted(sys.builtin_module_names))

print(textwrap.fill(name_text, width=64))
