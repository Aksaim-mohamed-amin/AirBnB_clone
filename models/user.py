#!/usr/bin/python3
""" This Modual contain the user class that inhertits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ This class defines the user modual and it attributes

    Attributes:
      email: User email (string)
      password: User password (string)
      first_name: User first name (string)
      last_name: User last name (string)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
