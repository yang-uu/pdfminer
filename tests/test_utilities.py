import unittest
from pdfminer.utils import url



class TestUtilities(unittest.TestCase):

    def test_url_basic(self):
        test_url = url("testsite.com/search?", name="John", lastname="Doe", age="25")
        self.assertEqual(test_url, "testsite.com/search?name=John&lastname=Doe&age=25")

    def test_url_special_characters(self):
        test_url = url("testsite.com/search?", name="Äööl_&==??!!  ")
        self.assertEqual(test_url, "testsite.com/search?name=%C3%84%C3%B6%C3%B6l_%26%3D%3D%3F%3F%21%21++")
    
    def test_url_empty(self):
        test_url = url("testsite.com/search?", name="")
        self.assertEqual(test_url, "testsite.com/search?name=")

if __name__ == '__main__':
    unittest.main()