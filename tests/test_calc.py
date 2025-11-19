import unittest
from my_functions import calculator, Operation

class TestCalculator(unittest.TestCase):

    def test_add_positive(self):
        actual_result = calculator(5, 3, Operation.ADD)
        self.assertEqual(actual_result, 8) 

    def test_add_negative(self):
        actual_result = calculator(5, -2, Operation.ADD)
        self.assertEqual(actual_result, 3) 

    def test_add_double_negative(self):
        actual_result = calculator(-3, -2, Operation.ADD)
        self.assertEqual(actual_result, -5) 

    def test_add_float(self):
        actual_result = calculator(3, 2.5, Operation.ADD)
        self.assertEqual(actual_result, 5.5) 

    def test_add_double_float(self):
        actual_result = calculator(3.1, 2.5, Operation.ADD)
        self.assertEqual(actual_result, 5.6) 

    def test_div_positive(self):
        actual_result = calculator(8, 2, Operation.DIVIDE)
        self.assertEqual(actual_result, 4) 

    def test_div_long_answer(self):
        actual_result = calculator(1, 3, Operation.DIVIDE)
        self.assertEqual(actual_result, 0.3333333333333333) 

    def test_div_float(self):
        actual_result = calculator(33.3, 3, Operation.DIVIDE)
        self.assertEqual(actual_result, 11.1) 

    def test_div_negative(self):
        actual_result = calculator(-9, 3, Operation.DIVIDE)
        self.assertEqual(actual_result, -3)

    def test_multiply_positive(self):
        actual_result = calculator(3, 3, Operation.MULTIPLY)
        self.assertEqual(actual_result, 9)

    def test_multiply_negative(self):
        actual_result = calculator(3, -3, Operation.MULTIPLY)
        self.assertEqual(actual_result, -9)

    def test_multiply_float(self):
        actual_result = calculator(3.4, 3, Operation.MULTIPLY)
        self.assertEqual(actual_result, 10.2)

    def test_subtract_positive(self):
        actual_result = calculator(9, 3, Operation.SUBTRACT)
        self.assertEqual(actual_result, 6)

    def test_subtract_negative(self):
        actual_result = calculator(9, -3, Operation.SUBTRACT)
        self.assertEqual(actual_result, 12)

    def test_subtract_float(self):
        actual_result = calculator(9, 3.5, Operation.SUBTRACT)
        self.assertEqual(actual_result, 5.5)


if __name__ == '__main__':
    unittest.main()
