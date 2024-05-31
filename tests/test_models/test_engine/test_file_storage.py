#!usr/bin/python3

import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage = storage

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_storage_instance(self):
        self.assertIsInstance(self.storage, FileStorage)

    def test_new(self):
        my_model = BaseModel()
        key = f"BaseModel.{my_model.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        my_model = BaseModel()
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        my_model = BaseModel()
        self.storage.save()
        key = f"BaseModel.{my_model.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
