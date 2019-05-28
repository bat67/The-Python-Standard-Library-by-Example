#!/usr/bin/env python3
# encoding: utf-8
"""
"""

#end_pymotw_header
import importlib

spec = importlib.util.find_spec('.submodule', package='example')
print('Loader:', spec.loader)

m = spec.loader.load_module()
print('Module:', m)
