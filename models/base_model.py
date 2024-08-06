#!/usr/bin/python3
"""
Base Model.
Defines all common attributes/methods for other classes.
"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """Initialize the BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
