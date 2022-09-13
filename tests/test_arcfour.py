import unittest
from pdfminer import arcfour


class TestArcFour(unittest.TestCase):
    def test_arcfour_encrypt(self) -> None:
        expected = 'bbf316e8d940af0ad3'
        result = arcfour.Arcfour(b'Key').process(b'Plaintext').hex()
        self.assertEqual(result, expected)

    def test_arcfour_encrypt2(self) -> None:
        expected = '1021bf0420'
        result = arcfour.Arcfour(b'Wiki').process(b'pedia').hex()
        self.assertEqual(result, expected)

    def test_arcfour_encrypt3(self) -> None:
        expected = '45a01f645fc35b383552544b9bf5'
        result = arcfour.Arcfour(b'Secret').process(b'Attack at dawn').hex()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
