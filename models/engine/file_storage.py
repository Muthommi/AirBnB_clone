#!/usr/bin/python3
"""This module defines the FileStorage class"""

import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes them back"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump(
                {key: obj.to_dict() for key, obj in self.__objects.items()},
                f
            )

    def reload(self):
        """Deserializes the JSON file to __objects, if it exists"""
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for key, value in objs.items():
                cls_name = value['__class__']
                cls = globals()[cls_name]
                self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            self.__objects = {}
