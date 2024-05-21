#!/usr/bin/python3
"""This model creates a user's details"""

from models.base_model.py import Basemodel


class user(BaseModel):
    def __init__(self, *arg, **kwargs):
        """Initializes a new user."""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
