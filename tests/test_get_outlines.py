import unittest
import os
from tools import dumppdf


class TestGetChaptersFromOutlines(unittest.TestCase):

    def setUp(self) -> None:

        self.course_book_pdf_file = os.path.join(
            os.path.dirname(__file__), '../samples/samples_for_chapter_retrieval/course_book_full.pdf'
        )

    def test_create_outline_length(self):
        chapter_names = dumppdf.get_chapters_from_outline(self.course_book_pdf_file)
        self.assertEqual(len(chapter_names), 25)

    def test_create_outline_first(self):
        chapter_names = dumppdf.get_chapters_from_outline(self.course_book_pdf_file)
        expected = 'Chapter 1: Changing Software'
        self.assertEqual(chapter_names[0], expected)

    def test_create_outline_last(self):
        chapter_names = dumppdf.get_chapters_from_outline(self.course_book_pdf_file)
        expected = 'Chapter 25: Dependency-Breaking Techniques'
        self.assertEqual(chapter_names[-1], expected)


if __name__ == '__main__':
    unittest.main()
