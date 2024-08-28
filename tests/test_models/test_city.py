#!/usr/bin/python3
"""
Unittest for the City class
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up a fresh City instance for each test."""
        self.city = City()

    def test_state_id_is_str(self):
        """Test that the city attribute state_id is a string"""
        self.assertIsInstance(self.city.state_id, str)

    def test_name_is_str(self):
        """Test that the city attribute name is a string"""
        self.assertIsInstance(self.city.name, str)
