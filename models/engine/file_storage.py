#!/usr/bin/python3
"""This module defines the FileStorage class."""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Simple file storage system for models"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self, obj=None):
        """Saves object to the file"""
        if obj:
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
        self._save_to_file()

    def _save_to_file(self):
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserializes objects to JSON file"""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                objects = json.load(f)
                for key, value in objects.items():
                    cls_name = value['__class__']
                    cls = globals()[cls_name]
                    self.__objects[key] = cls(**value)


storage = FileStorage()
storage.reload()
