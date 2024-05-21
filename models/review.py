#!/usr/bin/python3
"""Defines the Review class."""

from models.base.model import BaseModel


class Review(BaseModel):
    """This model creates a review class"""

    def __init__(self, *args, **kwargs):
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init(*args, **kwargs)
