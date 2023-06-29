#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):

    def test_init(self):
        # test case 1: rectangle with width 10 and height 5
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r1, Base)

    def test_init_with_id(self):
        # test case 1: rectangle with width 7, height 3, x 2, y 4, and id 1
        r2 = Rectangle(7, 3, 2, 4, 1)
        self.assertEqual(r2.width, 7)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 1)
        self.assertIsInstance(r2, Rectangle)
        self.assertIsInstance(r2, Base)

    def test_width(self):
        # test case 1: set width to 8
        r3 = Rectangle(10, 5)
        r3.width = 8
        self.assertEqual(r3.width, 8)

    def test_width_with_value_error(self):
        # test case 1: set width to -8, expect ValueError
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 5)
            r4.width = -8

    def test_width_with_type_error(self):
        # test case 1: set width to "8", expect TypeError
        with self.assertRaises(TypeError):
            r5 = Rectangle(10, 5)
            r5.width = "8"

    def test_height(self):
        # test case 1: set height to 3
        r6 = Rectangle(10, 5)
        r6.height = 3
        self.assertEqual(r6.height, 3)

    def test_height_with_value_error(self):
        # test case 1: set height to -3, expect ValueError
        with self.assertRaises(ValueError):
            r7 = Rectangle(10, 5)
            r7.height = -3

    def test_height_with_type_error(self):
        # test case 1: set height to "3", expect TypeError
        with self.assertRaises(TypeError):
            r8 = Rectangle(10, 5)
            r8.height = "3"

    def test_x(self):
        # test case 1: set x to 2
        r9 = Rectangle(10, 5)
        r9.x = 2
        self.assertEqual(r9.x, 2)

    def test_x_with_value_error(self):
        # test case 1: set x to -2, expect ValueError
        with self.assertRaises(ValueError):
            r10 = Rectangle(10, 5)
            r10.x = -2

    def test_x_with_type_error(self):
        # test case 1: set x to "2", expect TypeError
        with self.assertRaises(TypeError):
            r11 = Rectangle(10, 5)
            r11.x = "2"

    def test_y(self):
        # test case 1: set y to 4
        r12 = Rectangle(10, 5)
        r12.y = 4
        self.assertEqual(r12.y, 4)

    def test_y_with_value_error(self):
        # test case 1: set y to -4, expect ValueError
        with self.assertRaises(ValueError):
            r13 = Rectangle(10, 5)
            r13.y = -4

    def test_additional_type_error(self):
        # test case 1: set width to '', expect TypeError
        with self.assertRaises(TypeError):
            r14 = Rectangle('', 5)
            raise TypeError()

    def test_additional_type_error_2(self):
        # test case 1: set x to 1.50, expect TypeError
        with self.assertRaises(TypeError):
            Rectangle(5, 1, 45.90)
            raise TypeError()

if __name__ == '__main__':
    unittest.main()

