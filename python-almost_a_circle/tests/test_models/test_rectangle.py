#!/usr/bin/python3

from unittest.mock import patch
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_str(self):
        self.assertEqual(
            str(self.square),
            "[Square] (1) 2/3 - 5"
        )

    def test_size_getter(self):
        self.assertEqual(
            self.square.size,
            5
        )

    def test_size_setter(self):
        self.square.size = 10
        self.assertEqual(
            self.square.size,
            10
        )
        self.assertEqual(
            self.square.width,
            10
        )
        self.assertEqual(
            self.square.height,
            10
        )

    def test_update_args(self):
        self.square.update(2, 7, 4, 5)
        self.assertEqual(
            self.square.id,
            2
        )
        self.assertEqual(
            self.square.size,
            7
        )
        self.assertEqual(
            self.square.x,
            4
        )
        self.assertEqual(
            self.square.y,
            5
        )

    def test_update_kwargs(self):
        self.square.update(id=3, size=9, x=6, y=7)
        self.assertEqual(
            self.square.id,
            3
        )
        self.assertEqual(
            self.square.size,
            9
        )
        self.assertEqual(
            self.square.x,
            6
        )
        self.assertEqual(
            self.square.y,
            7
        )

    def test_to_dictionary(self):
        self.assertEqual(
            self.square.to_dictionary(),
            {
                "id": 1,
                "size": 5,
                "x": 2,
                "y": 3
            }
        )

if __name__ == '__main__':
    unittest.main()