#!/usr/bin/python3
"""Unittest for thw State class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests for the State class"""

    def setUp(self):
        """Sets up test environment"""
        self.state = State()

    def test_inheritance(self):
        """Test if State is a subclass of BaseModel"""
        self.aseertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Test attributes of State"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_attribute_types(self):
        """Test the types of State attributes"""
        self.assertIsInstance(self.state.name, str)


if __name__ == '__main__':
    unittest.main()
