#!/usr/bin/python3
"""Unittest for User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests the User class"""

    def setUp(self):
        """Sets up test environment"""
        self.user = User()

    def test_instance_creation(self):
        """Tests if the user instance is created correctly"""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Tests if the user has the correct attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_method(self):
        """Tests the __str__ method"""
        string = str(self.user)
        self.assertIn("[User]", string)
        self.assertIn("id", string)
        self.assertIn("created_at", string)
        self.assertIn("updated_at", string)

    def test_save_method(self):
        """Tests the save method"""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("id", user_dict)


if __name__ == '___main__':
    unittest.main()
