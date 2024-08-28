#!/usr/bin/python3
"""
Unittest for the State class
"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        """Set up a fresh State instance for each test."""
        self.state = State()

    def test_name_is_str(self):
        """Test that the state attribute name is a string"""
        self.assertIsInstance(self.state.name, str)
