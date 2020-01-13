#!/usr/bin/python3
"""Unittest for function max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function.

        Cases for integer and for types
    """

    def test_integers(self):
        """Test integers"""
        self.assertEqual(max_integer([1, 0, 3, 4, 5, 6]), 6)
        self.assertEqual(max_integer([1, 2, 6, 4, 5, 0]), 6)
        self.assertEqual(max_integer([6, 2, 3, 4, 0, 3]), 6)
        self.assertEqual(max_integer([-1, -2, -4, -3, 0, -5]), 0)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -1, -1]), -1)
        self.assertEqual(max_integer([0, -1, -2]), 0)

    def test_type(self):
        """Test different types"""
        self.assertEqual(max_integer("Texto Texto"), 'x')
        self.assertEqual(max_integer("Texto" "Zzzzzz"), 'z')
        self.assertEqual(max_integer(" "), ' ')
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, float('nan')]), 3)
        self.assertEqual(max_integer([1, 2, 3, float('inf')]), float('inf'))

if __name__ == '__main__':
    unittest.main()
