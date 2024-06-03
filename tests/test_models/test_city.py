#!/usr/bin/python3
"""Unit test for the city class"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def setUp(self):
        """Setup for City tests."""
        self.city = City()

    def test_instance_creation(self):
        """Tests if the city instance is created correctly"""
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """Tests if the city has the correct attributes"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_str_method(self):
        """Tests the __str__ method"""
        string = str(self.city)
        self.assertIn("[City]", string)
        self.assertIn("id", string)
        self.assertIn("created_at", string)
        self.assertIn("updated_at", string)

    def test_save_method(self):
        """Tests the save method"""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method"""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("id", city_dict)


if __name__ == '__main__':
    unittest.main()
