#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ class for testing max_integer function"""

    def test_unordered_maxint(self):
        """Test for different values unorder"""
        self.assertAlmostEqual(max_integer([1, 0, 3000, 4, 5, 10, 100]), 3000)
        self.assertAlmostEqual(max_integer([-1, -3000, -4, -5, -10, -100]), -1)
        self.assertAlmostEqual(max_integer([-1, 3000, -4, -5, 0, -100]), 3000)

    def test_ordered_maxint(self):
        """test for ordered"""
        self.assertAlmostEqual(max_integer([0, 1, 4, 5, 10, 100, 3000]), 3000)
        self.assertAlmostEqual(max_integer([-1, -3, -4, -5, -10, -3000]), -1)
        self.assertAlmostEqual(max_integer([-1, -3, -4, -5, 0, 3000]), 3000)

    def test_empty(self):
        """no input"""
        self.assertAlmostEqual(max_integer(), None)

    def test_notInt(self):
        """invalide arguements"""
        self.assertRaises(TypeError, max_integer, ["emeka", 1, 2, 3, 4])

if __name__ == '__name__':
    unittest.main()
