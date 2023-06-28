import unittest
from models.rectangle import Rectangle
import io
from unittest.mock import patch


class TestRectangle(unittest.TestCase):

    def test_width_type(self):
        self.assertRaises(TypeError, Rectangle, "2", 5)

    def test_width_value(self):
        self.assertRaises(ValueError, Rectangle, 0, 5)

    def test_height_type(self):
        self.assertRaises(TypeError, Rectangle, 2, "5")

    def test_height_value(self):
        self.assertRaises(ValueError, Rectangle, 2, -5)

    def test_x_type(self):
        self.assertRaises(TypeError, Rectangle, 2, 5, "3")

    def test_x_value(self):
        self.assertRaises(ValueError, Rectangle, 2, 5, -3)

    def test_y_type(self):
        self.assertRaises(TypeError, Rectangle, 2, 5, 3, "4")

    def test_y_value(self):
        self.assertRaises(ValueError, Rectangle, 2, 5, 3, -4)

    def test_area(self):
        rect = Rectangle(2, 5)
        self.assertEqual(rect.area(), 10)

    def setUp(self):
        self.rect = Rectangle(4, 4)
        self.output_stream = io.StringIO()

    def test_to_dictionary(self):
        rect = Rectangle(2, 5, 0, 0, 1)
        rect_dict = rect.to_dictionary()
        expected_dict = {'id': 1, 'width': 2, 'height': 5, 'x': 0, 'y': 0}
        self.assertEqual(rect_dict, expected_dict)

    def test_update_args(self):
        rect = Rectangle(2, 5)
        rect.update(1, 3, 4, 2, 1)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)

    def test_update_kwargs(self):
        rect = Rectangle(2, 5)
        rect.update(width=3, height=4, x=2, y=1)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)



if __name__ == '__main__':
    unittest.main()