#!/usr/bin/python3
""" Base Model Class """

import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all models in the AirBnB clone project.

    Attributes:
        id: UUID of the model instance.
        created_at: Timestamp of when the instance was created.
        updated_at: Timestamp of when the instance was last updated.
    """

    # Initiaisation
    def __init__(self):
        """
        Initializes a BaseModel instance.

        Args:
          *args: Unused positional arguments.
          **kwargs: Keyword arguments for the constructor.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    # Public Methodes
    def __str__(self):
        """ Return string representation of BaseModel instance """
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """ Updates the `updated_at` attribute with the current datetime. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
          dict: dictionary containing key-value pairs of instance attributes.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
