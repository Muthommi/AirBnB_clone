#!/usr/bin/python3
"""Unit tests for the Amenity class"""

import unittest
from models.amenity import Amenity
from datetime import datetime
import os


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Sets up test methods"""
        self.amenity = Amenity()

    def test_instance_creation(self):
        """Tests if the amenity instance is created correctly"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """Tests if the amenity has the correct attributes"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_str_method(self):
        """Tests the __str__ method"""
        string = str(self.amenity)
        self.assertIn("[Amenity]", string)
        self.assertIn("id", string)
        self.assertIn("created_at", string)
        self.assertIn("updated_at", string)

    def test_save_method(self):
        """Tests the save method"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("id", amenity_dict)


if __name__ == '__main__':
    unittest.main()
