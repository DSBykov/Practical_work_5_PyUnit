import unittest
from my_functions import is_even

class TestIsEven(unittest.TestCase):

    def test_even_num(self):
        even_numbers = [-2, 0, 2, 4, 2.0]
        for i in even_numbers:
            with self.subTest(i=i):
                self.assertTrue(is_even(i))

    def test_not_even_num(self):
        not_even_numbers = [-1, 1, 3, 2.2]
        for i in not_even_numbers:
            with self.subTest(i=i):
                self.assertFalse(is_even(i))


if __name__ == '__main__':
    unittest.main()
