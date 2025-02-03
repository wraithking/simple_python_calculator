import unittest
from Calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
# Sumesanas funckija
    def test_add(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(-2, 3), -5)
        self.assertEqual(subtract(-2, -3), 1)

    def test_subtraction(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(-2, 3), -5)
        self.assertEqual(subtract(-2, -3), 1)

    def test_multiplication(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-2, -3), 6)

    def test_division(self):
        self.assertAlmostEqual(divide(5, 2), 2.5)
        self.assertAlmostEqual(divide(0, 2), 0)
        self.assertRaises(ZeroDivisionError, divide, 5, 0)

if __name__ == '__main__':
    unittest.main()
