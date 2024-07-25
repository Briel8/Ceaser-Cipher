import unittest
from cipher import cipher

class TestCipher(unittest.TestCase):
    def test_cipher_for_a(self):
        self.assertEqual(cipher('a', 5), 'f')

    def test_cipher_for_z(self):
        self.assertEqual(cipher('z', 5), 'e')


if __name__ == '__main__':
    unittest.main()
