#!/usr/bin/python3
"""Defines the State class."""

from models.base.model import BaseModel


class State(BaseModel):
    """Defines attributes for a state."""

    def __init__(self, *args, **kwargs):
        """Initialize a new State instance."""
        self.name = ""
        super().__init__(*args, **kwargs)
