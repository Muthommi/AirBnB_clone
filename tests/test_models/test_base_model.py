#!/usr/bin/python3
"""Unit tests for the BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_init(self):
        """Test the initialization of the BaseModel instance"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict(self):
        """Test the to_dict method"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertEqual(obj_dict["created_at"], obj.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.isoformat())

    def test_save(self):
        """Test the save method"""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)


if __name__ == '__main__':
    unittest.main()
