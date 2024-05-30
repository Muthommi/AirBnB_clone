#!/usr/bin/python3
"""Unittest for the FileStorage class"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_initialization(self):
        """Test initialization of FileStorage"""
        file_path = self.storage._FileStorage__file_path
        objects = self.storage._FileStorage__objects
        self.assertEqual(file_path, "file.json")
        self.assertIsInstance(objects, dict)

    def test_all_method(self):
        """Test the all method of FileStorage"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), 0)

    def test_new_method(self):
        """Test the new method of FileStorage"""
        obj = BaseModel()
        obj_id = obj.id
        self.storage.new(obj)
        obj_key = "BaseModel." + obj_id
        self.assertIn(obj_key, self.storage._FileStorage__objects)

    def test_save_method(self):
        """Test the save method of FileStorage"""
        obj = BaseModel()
        obj_id = obj.id
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_method(self):
        """Test the reload method of FileStorage"""
        obj = BaseModel()
        obj_id = obj.id
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        obj_key = "BaseModel." + obj_id
        self.assertIn(obj_key, self.storage._FileStorage__objects)
        reloaded_obj = self.storage._FileStorage__objects[obj_key]
        self.assertIsInstance(reloaded_obj, BaseModel)
        self.assertEqual(reloaded_obj.to_dict(), obj.to_dict())


if __name__ == '__main__':
    unittest.main()
