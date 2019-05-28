#!/usr/bin/env python3
"""A test that fails with a custom message.
"""

#end_pymotw_header
import unittest


class FailureMessageTest(unittest.TestCase):

    def testFail(self):
        self.assertFalse(True, 'failure message goes here')
