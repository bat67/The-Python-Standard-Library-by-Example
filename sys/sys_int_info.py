#!/usr/bin/env python3
# encoding: utf-8
#end_pymotw_header
import sys

print('Number of bits used to hold each digit:',
      sys.int_info.bits_per_digit)
print('Size in bytes of C type used to hold each digit:',
      sys.int_info.sizeof_digit)
