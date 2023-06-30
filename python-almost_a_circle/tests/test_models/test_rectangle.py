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
    def test_value(self):
        self.assertRaisesRegex(
            ValueError, "width must be > 0", Rectangle, -1, 2)
    
    def test_type(self):
        self.assertRaisesRegex(
            TypeError, "width must be an integer", Rectangle, "1", 2)
    def test_to_dictionary(self):
        # Testing the conversion of object attributes to dictionary
        r = Rectangle(10, 5, 2, 4, 1)  # Create an instance of Rectangle
        expected_result = {
            "id": r.id,
            "width": r.width,
            "height": r.height,
            "x": r.x,
            "y": r.y
        }
        self.assertEqual(r.to_dictionary(), expected_result)


    def test_area_calculated_correctly(self):
        # Test case: area of rectangle with width 5 and height 10
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

        # Test case: area of rectangle with width 3 and height 7
        rect = Rectangle(3, 7)
        self.assertEqual(rect.area(), 21)

    def test_area_with_zero_width(self):
        # Test case: area of rectangle with width 0 and height 5
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 5)
            rect.area()
    def setUp(self):
        self.rectangle = Rectangle(2, 3)

    def test_update_with_args(self):
        self.rectangle.update(1, 2, 3, 4, 5)
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 2)
        self.assertEqual(self.rectangle.height, 3)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 5)

    def test_update_with_kwargs(self):
        self.rectangle.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 2)
        self.assertEqual(self.rectangle.height, 3)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 5)

    def test_update_with_args_and_kwargs(self):
        self.rectangle.update(1, 2, 3, x=4, y=5)
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 2)
        self.assertEqual(self.rectangle.height, 3)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 5)

    def test_create_rectangle(self):
        width = 2
        height = 3
        rectangle = Rectangle(width, height)

        self.assertEqual(rectangle.width, width)
        self.assertEqual(rectangle.height, height)

if __name__ == '__main__':
    unittest.main()


