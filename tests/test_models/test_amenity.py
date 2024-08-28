#!/usr/bin/python3
"""
Unittest for the Amenity class
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up a fresh Amenity instance for each test."""
        self.amenity = Amenity()

    def test_name_is_str(self):
        """Test that the Amenity attribute name is a string"""
        self.assertIsInstance(self.amenity.name, str)
