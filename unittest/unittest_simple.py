#!/usr/bin/env python3
"""Simplistic examples of unit tests.
"""

#end_pymotw_header
import unittest


class SimplisticTest(unittest.TestCase):

    def test(self):
        a = 'a'
        b = 'a'
        self.assertEqual(a, b)
