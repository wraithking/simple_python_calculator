import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        # Define the input to be provided to the calculator.py script
        input_data = '1\n2\n'

        # Run the calculator.py script and provide input
        process = subprocess.Popen(['python', 'calculator.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, error = process.communicate(input=input_data.encode())

        # Check that the output of the calculator.py script matches the expected output
        self.assertEqual(output.decode().strip(), '1.0 + 2.0 = 3.0')

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
