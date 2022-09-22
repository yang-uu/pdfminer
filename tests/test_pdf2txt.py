import unittest
import os

from tools.pdf2txt import (
    handle_input_variables,
    convert_from_pdf,
    ConverterParams,
    OutputType,
    split_by_chapters,
    write_chapters_to_files
    )
from pdfminer.layout import LAParams


class TestPdf2Text(unittest.TestCase):

    def test_convert_from_pdf_text(self):
        expected_output = ""
        expected_filename = os.path.join(
            os.path.dirname(__file__),
            'test_files/test_convert_from_pdf_text_expected.txt'
            )
        with open(expected_filename, 'r') as file:
            expected_output = file.read()

        test_filename = os.path.join(
            os.path.dirname(__file__),
            'test_files/test_convert_from_pdf_text_result.txt'
            )
        filename = [os.path.join(
            os.path.dirname(__file__),
            '../samples/simple1.pdf'
            )]
        convert_from_pdf(
            filename,
            ConverterParams(pagenos=set(), laparams=LAParams()),
            OutputType.TEXT,
            test_filename
        )

        # assert that the output file contains the expected output
        with open(test_filename, 'r') as file:
            contents = file.read()
            self.assertEqual(contents, expected_output)

    def test_convert_simple1_pdf_file_to_text(self):
        expected_filename = os.path.join(
            os.path.dirname(__file__),
            'test_files/test_convert_simple1_pdf_file_to_text_expected.txt'
        )
        with open(expected_filename, 'r') as file:
            expected_output = file.read()

        test_filename = os.path.join(
            os.path.dirname(__file__),
            'test_files/test_convert_simple1_pdf_file_to_text_result.txt'
        )
        options = [('-o', test_filename), ('-t', 'text')]
        filename = [os.path.join(
            os.path.dirname(__file__),
            '../samples/simple1.pdf'
            )]
        handle_input_variables(options, filename)

        # assert that the output file contains the expected output
        with open(test_filename, 'r') as file:
            contents = file.read()
            self.assertEqual(contents, expected_output)

    def test_convert_simple1_pdf_file_to_xml(self):
        expected_filename = os.path.join(
            os.path.dirname(__file__),
            'test_files/test_convert_simple1_pdf_file_to_xml_expected.xml'
            )
        with open(expected_filename, 'r') as file:
            expected_output = file.read()

        test_filename = os.path.join(
            os.path.dirname(__file__),
            'test_files/test_convert_simple1_pdf_file_to_xml_result.xml'
            )
        options = [('-o', test_filename), ('-t', 'xml')]
        filename = [os.path.join(
            os.path.dirname(__file__),
            '../samples/simple1.pdf'
            )]
        handle_input_variables(options, filename)

        # assert that the output file contains the expected output
        with open(test_filename, 'r') as file:
            contents = file.read()
            self.assertEqual(contents, expected_output)

    def test_convert_simple1_pdf_file_to_html(self):
        expected_filename = os.path.join(
            os.path.dirname(__file__),
            'test_files/test_convert_simple1_pdf_file_to_html_expected.html'
            )
        with open(expected_filename, 'r') as file:
            expected_output = file.read()

        test_filename = os.path.join(
            os.path.dirname(__file__),
            'test_files/test_convert_simple1_pdf_file_to_html_result.html'
            )
        options = [('-o', test_filename), ('-t', 'html')]
        filename = [os.path.join(
            os.path.dirname(__file__),
            '../samples/simple1.pdf'
            )]
        handle_input_variables(options, filename)

        # assert that the output file contains the expected output
        with open(test_filename, 'r') as file:
            contents = file.read()
            self.assertEqual(contents, expected_output)


class TestPdf2Chapters(unittest.TestCase):

    def setUp(self) -> None:

        self.course_book_txt_file = os.path.join(
            os.path.dirname(__file__), '../samples/samples_for_chapter_retrieval/course_book_full.txt'
        )
        self.course_book_pdf_file = os.path.join(
            os.path.dirname(__file__), '../samples/samples_for_chapter_retrieval/course_book_full.pdf'
        )

    def test_split_txt_file_by_chapters(self):
        chapters = split_by_chapters(self.course_book_txt_file)
        expected_length = 26
        self.assertEqual(len(chapters), expected_length)

    def test_write_chapters_to_txt_files(self):
        test_chapter_path = os.path.join(
            os.path.dirname(__file__), 'test_chapters/'
        )
        chapters = split_by_chapters(self.course_book_txt_file)
        write_chapters_to_files(chapters, path=test_chapter_path)


if __name__ == '__main__':
    unittest.main()
