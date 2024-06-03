#!/usr/bin/python3
"""
Unittests for the FileStorage class.
"""

import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test suite for FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """Test that new adds an object to the storage"""
        obj = BaseModel()
        key = f"BaseModel.{obj.id}"
        self.storage.new(obj)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save(self):
        """Test that save correctly serializes objects to the JSON file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, data)
        self.assertEqual(data[key]['id'], obj.id)

    def test_reload(self):
        """Test that reload correctly deserializes objects from the JSON file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, obj.id)

    def test_reload_with_empty_file(self):
        """Test that reload works correctly with an empty file"""
        open(self.file_path, 'w').close()
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_new_with_all_classes(self):
        """Test new with all classes"""
        classes = [BaseModel, User, State, City, Amenity, Place, Review]
        for cls in classes:
            obj = cls()
            key = f"{cls.__name__}.{obj.id}"
            self.storage.new(obj)
            self.assertIn(key, self.storage.all())
            self.assertEqual(self.storage.all()[key], obj)

    def test_reload_with_all_classes(self):
        """Test reload with all classes"""
        classes = [BaseModel, User, State, City, Amenity, Place, Review]
        for cls in classes:
            obj = cls()
            self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        for cls in classes:
            obj = cls()
            key = f"{cls.__name__}.{obj.id}"
            self.assertIn(key, self.storage.all())
            self.assertEqual(self.storage.all()[key].id, obj.id)


if __name__ == '__main__':
    unittest.main()
