from utils import Utils
import unittest

class TestUtils(unittest.TestCase):

    def test_reversed(self):
        self.assertEqual(Utils.reversed(123), 321)
        self.assertRaises(AssertionError, Utils.reversed,"123")
        self.assertRaises(AssertionError, Utils.reversed, 123.1)

    def test_formatter(self):
        self.assertEqual(Utils.formatter(123),('0b1111011','0o173'))
        self.assertRaises(AssertionError, Utils.formatter,"123")
        self.assertRaises(AssertionError, Utils.formatter, 123.1)

if __name__ == '__main__':
    unittest.main()