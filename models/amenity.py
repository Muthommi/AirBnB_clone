#!/usr/bin/python3
"""Defines the Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This model creates Amenity class."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity class."""
        super().__init__(*args, **kwargs)
