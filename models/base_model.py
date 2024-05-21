#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines attributes for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if (hasattr(self, 'created_at') and
                    isinstance(self.created_at, str)):
                self.created_at = datetime.strptime(
                    self.created_at, '%Y-%m-%dT%H:%M:%S.%f'
                )
            if (hasattr(self, 'updated_at') and
                    isinstance(self.updated_at, str)):
                self.updated_at = datetime.strptime(
                    self.updated_at, '%Y-%m-%dT%H:%M:%S.%f'
                )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates updated_at and saves the object"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result

    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
