#!/usr/bin/python3
"""Define the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user and it attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
