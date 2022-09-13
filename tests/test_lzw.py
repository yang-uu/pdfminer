from pdfminer.lzw import lzwdecode


import unittest


class TestLzwDecode(unittest.TestCase):

    # lzwdecode
    def test_lzwdecode(self):
        self.assertEqual(lzwdecode(
            bytes.fromhex('800b6050220c0c8501')), b'-----A---B')


if __name__ == '__main__':
    unittest.main()
