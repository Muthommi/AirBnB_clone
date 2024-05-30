#!/usr/bin/python3

import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Setup for Place tests."""
        self.place = Place()

    def test_inheritance(self):
        """Tests place inherits from BaseModel."""
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Tests that place has the correct attributes."""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.asserTrue(hasattr(self.place, "description"))
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

    def test_id_is_uuid(self):
        """Tests that the uuid is valid."""
        self.assertIsInstance(uuid.UUID(self.place.id), uuid.UUID)

    def test_created_at_is_datetime(self):
        """Tests created_at is a datetime object."""
        self.assertIsInstance(self.place.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Tests updated_at is a datetime object."""
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_to_dict(self):
        """Tests to_dict method."""
        place_dict + self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], self.place.id)
        self.assertEqual(place_dict['created_at'],
                         self.place.created_at.isoformat())
        self.assertEqual(place_dict['updated_at'],
                         self.place.updated_at.isoformat())

        def test_save(self):
            """Tests save method updates 'updated_at' attribute."""
            old_updated_at = self.place.updated_at
            self.place.save()
            self.assertNotEqual(old_updated_at, self.place.updated_at)


if __name__ == '__main__':
    unittest.main()
