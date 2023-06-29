#!/usr/bin/python3
# test_square.py
"""Defines unittests for models/square.py.
"""

import unittest
from models.square import Square
import io
import sys
import unittest
from models.base import Base


class TestSquare(unittest.TestCase):

    
    def test_str(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_size_getter(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_size_setter(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_update_args(self):
        square = Square(5, 2, 3, 1)
        square.update(2, 10, 4, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def test_update_kwargs(self):
        square = Square(5, 2, 3, 1)
        square.update(id=2, size=10, x=4, y=5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()