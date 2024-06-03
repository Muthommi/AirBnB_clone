#!/usr/bin/python3

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for class Place"""

    def setUp(self):
        """Setup for Place tests."""
        self.place = Place()

    def test_instance_creation(self):
        """Tests if place instance is correctly created."""
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        """Tests that place has the correct attributes."""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_str_method(self):
        """Test the __str__ method"""
        string = str(self.place)
        self.assertIn("[Place]", string)
        self.assertIn("id", string)
        self.assertIn("created_at", string)
        self.assertIn("updated_at", string)

    def test_save_method(self):
        """Tests save method updates 'updated_at' attribute."""
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertIn("id", place_dict)


if __name__ == '__main__':
    unittest.main()
