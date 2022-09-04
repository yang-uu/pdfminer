#!/usr/bin/env python

import unittest
from pdfminer.runlength import rldecode


class TestRunLength(unittest.TestCase):

    def test_rldecode(self):
        input = b'\x05123456\xfa7\x04abcde\x80junk'
        result = rldecode(input)
        expected = b'1234567777777abcde'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
