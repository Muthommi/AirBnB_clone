#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """Defines attributes for other classes."""

    def __init___(self, *args, **kwargs):
        """Initialize anew Basemodel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, "%Y%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all values of the instance."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """Return the string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
