#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initializes the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns string representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates public instance attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with keys/values of __dict__ of the instance"""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
