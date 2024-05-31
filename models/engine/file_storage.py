#!/usr/bin/python3

import json
import os
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary objects."""
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes objects to JSON file"""
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as f:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        cls_name = value['__class__']
                        cls = globals().get(cls_name)
                        if cls:
                            FileStorage.__objects[key] = cls(**value)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                pass
