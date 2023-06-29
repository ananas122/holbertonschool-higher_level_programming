import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json
import os


# Define a test class TestBase
class TestBase(unittest.TestCase):

    # Test method to check base id generation
    def test_base_id_generation(self):
        base1 = Base()
        base2 = Base()
        base3 = Base(89)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 89)

    # Test method to check Base.to_json_string with None argument
    def test_base_to_json_string_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    # Test method to check Base.to_json_string with empty list argument
    def test_base_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    # Test method to check Base.to_json_string with data argument
    def test_base_to_json_string_with_data(self):
        json_string = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_string, '[{"id": 12}]')

    # Test method to check Base.to_json_string returns a string
    def test_base_to_json_string_with_data_returning_string(self):
        json_string = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(json_string, str)

    # Test method to check Base.from_json_string with None argument
    def test_base_from_json_string_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    # Test method to check Base.from_json_string with empty list argument
    def test_base_from_json_string_empty_list(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    # Test method to check Base.from_json_string with data argument
    def test_base_from_json_string_with_data(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{'id': 89}])

    # Test method to check Base.from_json_string returns a list
    def test_base_from_json_string_with_data_returning_list(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
