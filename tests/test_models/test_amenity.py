#!/usr/bin/python3
"""Unit tests for the Amenity class"""

import unittest
from models.amenity import Amenity
from datetime import datetime
import os


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up test methods"""
        self.amenity = Amenity()
        self.amenity.name = "Pool"
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up after each test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """Test the initialization of the Amenity instance"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertEqual(self.amenity.name, "Pool")

    def test_to_dict(self):
        """Test the to_dict method"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(amenity_dict["id"], self.amenity.id)
        self.assertEqual(amenity_dict["created_at"],
                         self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict["updated_at"],
                         self.amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict["name"], self.amenity.name)

    def test_save(self):
        """Test the save method"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
