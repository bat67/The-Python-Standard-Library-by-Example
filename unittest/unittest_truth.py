#!/usr/bin/env python3
"""Test for truth
"""

#end_pymotw_header
import unittest


class TruthTest(unittest.TestCase):

    def testAssertTrue(self):
        self.assertTrue(True)

    def testAssertFalse(self):
        self.assertFalse(False)
