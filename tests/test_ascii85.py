import unittest

from pdfminer.ascii85 import ascii85decode, asciihexdecode


class TestAscii85(unittest.TestCase):

    def test_ascii85_decode(self) -> None:
        self.assertEqual(
            ascii85decode(b'9jqo^BlbD-BleB1DJ+*+F(f,q'),
            b'Man is distinguished'
        )
        self.assertEqual(ascii85decode(b'E,9)oF*2M7/c~>'), b'pleasure.')

    def test_ascii_hex_decode(self) -> None:

        self.assertEqual(asciihexdecode(b'61 62 2e6364   65'), b'ab.cde')
        self.assertEqual(asciihexdecode(b'61 62 2e6364   657>'), b'ab.cdep')
        self.assertEqual(asciihexdecode(b'7>'), b'p')


if __name__ == '__main__':
    unittest.main()
