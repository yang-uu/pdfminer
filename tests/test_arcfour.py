import unittest
from pdfminer import arcfour


class TestArcFour(unittest.TestCase):
    def test_arcfour_encrypt(self) -> None:
        self.assertEqual(arcfour.Arcfour(b'Key').process(b'Plaintext').hex(), 'bbf316e8d940af0ad3')

    def test_arcfour_encrypt2(self) -> None:
        self.assertEqual(arcfour.Arcfour(b'Wiki').process(b'pedia').hex(), '1021bf0420')

    def test_arcfour_encrypt3(self) -> None:
        self.assertEqual(arcfour.Arcfour(b'Secret').process(b'Attack at dawn').hex(), '45a01f645fc35b383552544b9bf5')


if __name__ == '__main__':
    unittest.main()
