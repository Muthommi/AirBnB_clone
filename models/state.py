#!/usr/bin/python3
"""Defines the State class."""

from models.base_model import BaseModel


class State(BaseModel):
    """Defines attributes for a state."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new State instance."""
        super().__init__(*args, **kwargs)
