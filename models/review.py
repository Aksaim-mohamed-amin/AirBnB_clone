#!/usr/bin/python3
"""Define the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines a Review and it attributes"""
    place_id = ''
    user_id = ''
    text = ''
