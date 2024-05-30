#!/usr/bin/python3
"""Unittest for User class"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests the User class"""

    def setUp(self):
        """Sets up test environment"""
        self.user = User()

    def test_inheritance(self):
        """Tests if User is a subclass of BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Tests the attribute of the user"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")

    def test_attribute_types(self):
        """Test the type of user attributes"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsinstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)


if __name__ == '___main__':
    unittest.main()
