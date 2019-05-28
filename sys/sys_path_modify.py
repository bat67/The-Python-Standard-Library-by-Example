#!/usr/bin/env python3
# encoding: utf-8
"""
"""
#end_pymotw_header
import importlib
import os
import sys

base_dir = os.path.dirname(__file__) or '.'
print('Base directory:', base_dir)

# Insert the package_dir_a directory at the front of the path.
package_dir_a = os.path.join(base_dir, 'package_dir_a')
sys.path.insert(0, package_dir_a)

# Import the example module
import example
print('Imported example from:', example.__file__)
print('  ', example.DATA)

# Make package_dir_b the first directory in the search path
package_dir_b = os.path.join(base_dir, 'package_dir_b')
sys.path.insert(0, package_dir_b)

# Reload the module to get the other version
importlib.reload(example)
print('Reloaded example from:', example.__file__)
print('  ', example.DATA)
