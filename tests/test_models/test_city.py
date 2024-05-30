#!/usr/bin/python3
"""Unit test for the city class"""


import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestCity(unittest.TestCase):
    def setUp(self):
        """Setup for City tests."""
        self.city = City()

    def test_inheritance(self):
        """Test that City inherits from BaseModel."""
        self.assertIsInstance(self.city, BaseModel)

    def test_id_attribute(self):
        """Tests the type and initial value of the state_id attribute."""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertIsInstance(self.city.state_id, str)
        self.assertEqual(self.city.state_id, "")

    def test_name_attribute(self):
        """Tests bot name and initial value of the name attribute"""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertIsInstance(self.city.name, str)
        self.assertEqual(self.city.name, "")

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        self.assertIsInstance(self.city.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime oject"""
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_to_dict(self):
        """Test the to_dict method."""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], self.city.state_id)
        self.assertEqual(city_dict['name'], self.city.name)

    def test_save(self):
        """Test the save method updates `updated_at` attribute."""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)


if __name__ == '__main__':
    unittest.main()
