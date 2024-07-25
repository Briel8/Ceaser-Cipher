import unittest
from cipher import ceaser_cipher

class TestCeaserCipher(unittest.TestCase):
    def test_ceaser_cipher_brian(self):
        self.assertEqual(ceaser_cipher('brian', 5), 'Gwnfs')


if __name__ == '__main__':
    unittest.main()