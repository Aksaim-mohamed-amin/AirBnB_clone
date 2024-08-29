#!/usr/bin/python3
"""
Unit test for the Airbnb console
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Tests the Airbnb console"""

    def setUp(self):
        """Set up for tests"""
        self.cmd = HBNBCommand()
        self.models = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                       'Place', 'Review']
        self.commands = ['EOF', 'all', 'count' ,'create' ,'destroy' ,'help',
                         'quit' ,'show', 'update']

    def test_help_create(self):
        """Test the help documentation for all the commands"""
        for command in self.commands:
            with patch('sys.stdout', new=StringIO()) as f:
                self.cmd.onecmd(f"help {command}")
                doc = f.getvalue().strip()
                self.assertTrue(len(doc) > 0)

    def test_create(self):
        """"Test the creation of all type of models"""
        for model in self.models:
            with patch('sys.stdout', new=StringIO()) as f:
                self.cmd.onecmd(f"create {model}")
                id = f.getvalue().strip()
                self.assertTrue(len(id) > 0)
