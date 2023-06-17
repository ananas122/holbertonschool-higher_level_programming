#!/usr/bin/python3

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([4, -3, 2, -1]), 4)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 4]), 4)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

if __name__ == '__main__':
    unittest.main()
