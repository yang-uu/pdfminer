# coding: utf-8

import unittest
import os

from tools.dumppdf import dumpoutline


class TestDumpPDF(unittest.TestCase):

    def test_dumpoutline(self):
        output_filename = "./test_dumpoutline.test.out"
        with open(output_filename, "w") as fp:
            dumpoutline(fp, "./samples/test_dumpoutline.pdf", None, None)
        with open(output_filename) as fp:
            result = fp.read()
        os.remove(output_filename)
        with open("./samples/test_dumpoutline.out") as fp:
            correct = fp.read()
        self.assertEqual(result, correct)


if __name__ == '__main__':
    unittest.main()
