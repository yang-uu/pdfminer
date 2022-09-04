
#!/usr/bin/env python

from rijndael import *

import unittest

class TestRijndael(unittest.TestCase):

    def test_RinjndaelDecryptor(self):
        key = bytes.fromhex('00010203050607080a0b0c0d0f101112')
        ciphertext = bytes.fromhex('d8f532538289ef7d06b506a4fd5be9c9')
        answer = RijndaelDecryptor(key, 128).decrypt(ciphertext).hex()
        self.assertEqual(answer, '506812a45f08c889b97f5980038b8359')

    def test_RinjndaelEncryptor(self):
        key = bytes.fromhex('00010203050607080a0b0c0d0f101112')
        plaintext = bytes.fromhex('506812a45f08c889b97f5980038b8359')
        answer = RijndaelEncryptor(key, 128).encrypt(plaintext).hex()
        self.assertEqual(answer, 'd8f532538289ef7d06b506a4fd5be9c9')

if __name__ == '__main__':
    unittest.main()
