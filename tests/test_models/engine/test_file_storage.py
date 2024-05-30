#!/usr/bin/python3
"""Unit tests for the FileStorage class"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Setup the test environment"""
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Clean up the test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test that all() returns the __objects dictionary"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test that new() adds an object to __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test that save() serializes __objects to a JSON file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, 'r') as f:
            content = json.load(f)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, content)

    def test_reload(self):
        """Test that reload() deserializes the JSON file to __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
