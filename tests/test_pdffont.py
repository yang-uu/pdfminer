import os
import unittest
from tools.dumppdf import dumpfontnames


class TestPDFFont(unittest.TestCase):

    def _test(self, test_pdf_filename, correct_output_file):
        output_filename = "./tests/test_files/test_dumpfontnames_result.out"

        with open(output_filename, "w") as fp:
            dumpfontnames(fp, test_pdf_filename, None, None)
        with open(output_filename) as fp:
            result = fp.read()
        os.remove(output_filename)
        with open(correct_output_file) as fp:
            correct = fp.read()
        self.assertEqual(result, correct)

    def test_arial(self):
        self._test(
            "./tests/test_files/dumpfontnames/test_pdffont_arial.pdf",
            "./tests/test_files/dumpfontnames/test_pdffont_arial_expected.out")

    def test_timesnewroman_arial(self):
        self._test(
            "./tests/test_files/dumpfontnames/test_timesnewroman_arial.pdf",
            "./tests/test_files/dumpfontnames/test_timesnewroman_arial_expected.out")

    def test_timesnewroman_arial_verdana(self):
        self._test(
            "./tests/test_files/dumpfontnames/test_timesnewroman_arial_verdana.pdf",
            "./tests/test_files/dumpfontnames/test_timesnewroman_arial_verdana_expected.out")


if __name__ == "__main__":
    unittest.main()
