#!/usr/bin/python3
"""
FileStorage module for serializing and deserializing objects.
"""

import json
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes them back to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, 'w') as f:
            obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file exists)."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                if os.stat(FileStorage.__file_path).st_size == 0:
                    return
                obj_dict = json.load(f)
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review

                classes = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review
                }

                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    if cls_name in classes:
                        self.new(classes[cls_name](**value))
        except FileNotFoundError:
            pass
