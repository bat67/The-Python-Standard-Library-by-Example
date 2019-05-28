#!/usr/bin/env python3
"""Demonstrate possible test outcomes
"""

#end_pymotw_header
import unittest


class OutcomesTest(unittest.TestCase):

    def testPass(self):
        return

    def testFail(self):
        self.assertFalse(True)

    def testError(self):
        raise RuntimeError('Test error!')
