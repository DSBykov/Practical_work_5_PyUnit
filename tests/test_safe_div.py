import unittest
from my_functions import safe_divide


class TestSafeDivide(unittest.TestCase):

    def test_divide_by_zero_too(self):
        with self.assertRaises(ZeroDivisionError):
            safe_divide(8, 0)

if __name__ == '__main__':
    unittest.main()
