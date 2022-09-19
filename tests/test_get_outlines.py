import unittest
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from tools import dumppdf


class TestGetChaptersFromOutlines(unittest.TestCase):

    def test_create_outline_length(self):
        file_name = '../samples/samples_for_chapter_retrieval/course_book_full.pdf'
        chapter_names = dumppdf.get_chapters_from_outline(file_name)
        self.assertEqual(len(chapter_names), 25)

    def test_create_outline_first(self):
        file_name = '../samples/samples_for_chapter_retrieval/course_book_full.pdf'
        chapter_names = dumppdf.get_chapters_from_outline(file_name)
        expected = 'Chapter 1: Changing Software'
        self.assertEqual(chapter_names[0], expected)

    def test_create_outline_last(self):
        file_name = '../samples/samples_for_chapter_retrieval/course_book_full.pdf'
        chapter_names = dumppdf.get_chapters_from_outline(file_name)
        expected = 'Chapter 25: Dependency-Breaking Techniques'
        self.assertEqual(chapter_names[-1], expected)



if __name__ == '__main__':
    unittest.main()