import unittest
from pathlib import Path
import os

from tools.pdf2txt import handle_input_variables, convert_from_pdf, ConverterParams, OutputType
from pdfminer.layout import LAParams


class TestPdf2Text(unittest.TestCase):

    def test_convert_from_pdf_text(self):
        expected_output = ""
        expected_filename = 'test_files/test_convert_from_pdf_text_expected.txt'
        with open(expected_filename, 'r') as file:
            expected_output = file.read()

        test_filename = 'test_files/test_convert_from_pdf_text_result.txt'
        filename = ['../samples/simple1.pdf']
        convert_from_pdf(filename, ConverterParams(pagenos=set(), laparams=LAParams()), OutputType.TEXT, test_filename)

        # assert that the output file contains the expected output
        with open(test_filename, 'r') as file:
            contents = file.read()
            self.assertEqual(contents, expected_output)

    def test_convert_simple1_pdf_file_to_text(self):
        expected_filename = os.path.join(PATH, 'test_files/test_convert_simple1_pdf_file_to_text_expected.txt')
        with open(expected_filename, 'r') as file:
            expected_output = file.read()

        test_filename = 'test_files/test_convert_simple1_pdf_file_to_text_result.txt'
        options = [('-o', test_filename), ('-t', 'text')]
        filename = ['../samples/simple1.pdf']
        handle_input_variables(options, filename)

        # assert that the output file contains the expected output
        with open(test_filename, 'r') as file:
            contents = file.read()
            self.assertEqual(contents, expected_output)

    def test_convert_simple1_pdf_file_to_xml(self):
        expected_filename = 'test_files/test_convert_simple1_pdf_file_to_xml_expected.xml'
        with open(expected_filename, 'r') as file:
            expected_output = file.read()

        test_filename = 'test_files/test_convert_simple1_pdf_file_to_xml_result.xml'
        options = [('-o', test_filename), ('-t', 'xml')]
        filename = ['../samples/simple1.pdf']
        handle_input_variables(options, filename)

        # assert that the output file contains the expected output
        with open(test_filename, 'r') as file:
            contents = file.read()
            self.assertEqual(contents, expected_output)

    def test_convert_simple1_pdf_file_to_html(self):
        expected_filename = 'test_files/test_convert_simple1_pdf_file_to_html_expected.html'
        with open(expected_filename, 'r') as file:
            expected_output = file.read()

        test_filename = 'test_files/test_convert_simple1_pdf_file_to_html_result.html'
        options = [('-o', test_filename), ('-t', 'html')]
        filename = ['../samples/simple1.pdf']
        handle_input_variables(options, filename)

        # assert that the output file contains the expected output
        with open(test_filename, 'r') as file:
            contents = file.read()
            self.assertEqual(contents, expected_output)


if __name__ == '__main__':
    unittest.main()
