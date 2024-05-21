#!/usr/bin/python3
"""Defines a city class."""

from models.base_model import BaseModel


class City(BaseModel):
    """This model creates a city model"""

    def __init__(self, *args, **kwargs):
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
