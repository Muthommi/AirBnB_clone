#!/usr/bin/python3
"""Unittest for thw State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests for the State class"""

    def setUp(self):
        """Sets up test environment"""
        self.state = State()

    def test_inheritance(self):
        """Test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """Test attributes of State"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_str_method(self):
        """Test the __str__ method"""
        string = str(self.state)
        self.assertIn("[State]", string)
        self.assertIn("id", string)
        self.assertIn("created_at", string)
        self.assertIn("updated_at", string)

    def test_save_method(self):
        """Test the save method"""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("id", state_dict)


if __name__ == '__main__':
    unittest.main()
