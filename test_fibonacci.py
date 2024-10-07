import unittest

from Fibonacci import main,Fibonacci_

class TestFibonacci(unittest.TestCase):
    def test_n_23(self):
        self.assertEqual(Fibonacci_(23),28657)
    def test_negative_n(self):
        self.assertFalse(Fibonacci_(-6))
    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            int('invalid')
if __name__=='__main__':
    unittest.main()
