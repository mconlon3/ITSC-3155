import unittest
from calculator import Calculator
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(3, 2), 5)
        self.assertEqual(Calculator.add(6, 7), 13)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(4, 2), 2)
        self.assertEqual(Calculator.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3, 2), 6)
        self.assertEqual(Calculator.multiply(6, 1), 6)

    def test_divide(self):
        self.assertEqual(Calculator.divide(8, 4), 2)
        self.assertEqual(Calculator.divide(4, 4), 1)

if __name__ == "__main__":
    unittest.main()