import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

class CalculatorTests(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(7, 3), 10)

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(10, 5), 5)

if __name__ == '__main__':
    unittest.main()
