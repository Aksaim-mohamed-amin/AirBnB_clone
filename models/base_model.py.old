#!/usr/bin/python3
"""BaseModel Module.

This module defines the BaseModel class that serves as a base class for other
models in the AirBnb Clone project.
It include common attributes and methods for other classes.
"""


import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel class.
    
    This class defines all common attributes/methods for other classess.
    """

    def __init__(self):
        """Initialize a new BaseModel instance.

        assigns a unique ID and time stamp to the instance created.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance.

        Returns:
        A string in the format [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the public instance attribute updated_at 
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance.

        Returns:
            dict: A dictionary representation of the instance with class name and
            ISO format dates for created_at and updated_at.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
